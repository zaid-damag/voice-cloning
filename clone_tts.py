import gradio as gr
import os
import tempfile
import numpy as np
import torch
import soundfile as sf
import librosa
from TTS.api import TTS
import wavmark

# دالة لتحويل الصوت إلى أحادي 16kHz
def ensure_mono_16k(y, sr):
    if y.ndim == 2:  # ستيريو إلى أحادي
        y = np.mean(y, axis=1)
    if sr != 16000:
        y = librosa.resample(y, orig_sr=sr, target_sr=16000)
        sr = 16000
    return y, sr

# دالة لإضافة علامة مائية
def add_watermark(in_wav_path, out_wav_path, payload_bits=16):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = wavmark.load_model().to(device)
    y, sr = sf.read(in_wav_path, always_2d=False)
    y16, _ = ensure_mono_16k(y, sr)
    payload = np.random.choice([0, 1], size=payload_bits)
    y_wm, _ = wavmark.encode_watermark(model, y16, payload, show_progress=False)
    sf.write(out_wav_path, y_wm, 16000)

# دالة لاستنساخ الصوت
def clone_voice(reference_audio, text, language):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

    with tempfile.TemporaryDirectory() as td:
        tmp = os.path.join(td, "tmp.wav")
        tts.tts_to_file(
            text=text,
            speaker_wav=reference_audio,
            language=language,
            file_path=tmp
        )

        output_path = "output.wav"
        add_watermark(tmp, output_path)

    return output_path

# واجهة مستخدم باستخدام Gradio
iface = gr.Interface(
    fn=clone_voice,
    inputs=[
        gr.Audio(sources=["upload"], type="filepath", label="تسجيل الصوت المرجعي"),
        gr.Textbox(label="النص المراد تحويله إلى كلام"),
        gr.Dropdown(["ar", "en", "he"], label="اللغة", value="ar")
    ],
    outputs=gr.Audio(label="الصوت المستنسخ"),
    title="استنساخ الصوت باستخدام XTTS-v2",
    description="قم بتحميل تسجيل صوت مرجعي، أدخل النص، واختر اللغة (العربية/الإنجليزية/العبرية)."
)

iface.launch()
