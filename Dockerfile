# استخدم صورة بايثون 3.11 من Docker Hub
FROM python:3.11-slim

# تعيين مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ جميع ملفات المشروع إلى الحاوية
COPY . /app

# نسخ requirements.txt إلى الحاوية
COPY requirements.txt /app/

# تثبيت pip وتحديثه
RUN pip install --upgrade pip

# تثبيت التبعيات باستخدام pip
RUN pip install -r requirements.txt

# فتح المنفذ إذا كان لديك تطبيق ويب يعمل على الحاوية (اختياري)
EXPOSE 8000

# تشغيل السكربت الرئيسي باستخدام Python
CMD ["python", "clone_tts.py", "--ref", "data/ref.wav", "--text", "This is a voice cloning example."]
