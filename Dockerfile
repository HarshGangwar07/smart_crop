# Base image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y git

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements and install
COPY requirements.txt .
RUN pip install --default-timeout=100 --retries=5 --no-cache-dir -r requirements.txt

# Copy project files (make sure manage.py is copied before next step)
COPY . .

# Set environment variables (modern format)
ENV DJANGO_SETTINGS_MODULE=smart_crop.settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Run the application
CMD ["gunicorn", "smart_crop.wsgi:application", "--bind", "0.0.0.0:8000"]
