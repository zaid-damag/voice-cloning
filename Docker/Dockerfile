# استخدم صورة بايثون 3.11 من Docker Hub
FROM python:3.11-slim

# تعيين مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ جميع ملفات المشروع إلى الحاوية
COPY . /app

# تثبيت pip وتحديثه
RUN pip install --upgrade pip

# تثبيت التبعيات باستخدام pip
RUN pip install -r requirements.txt

# فتح المنفذ لواجهة Gradio
EXPOSE 7860

# تشغيل تطبيق Gradio
CMD ["python", "app.py"]
