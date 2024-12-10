# # FROM python:3
# # COPY . /user/src/app
# # WORKDIR /user/src/app
# # RUN pip3 install -r requirements.txt
# # CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
# # CMD ["python3", "./app/manage.py", "runserver"]
# # Use an official Python runtime as a parent image
# FROM python:3.11-slim

# RUN apt-get update -qq \
#   && apt-get install -y curl \
#   && apt-get clean \
#   && rm -rf /var/lib/apt/lists/*

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # Set work directory
# WORKDIR /code

# # Install dependencies
# COPY requirements.txt /code/
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy project
# COPY . /code/

# # Collect static files
# RUN python manage.py collectstatic --noinput

# # Start server
# CMD python manage.py migrate && python manage.py createsuperauto && gunicorn defang_sample.wsgi:application --bind 0.0.0.0:8000
# FROM python:3.9.6
# ENV env 1
# WORKDIR /webpage
# COPY requirements.txt /app/requirements.txt
# RUN pip install -r requirements.txt
# COPY . /app


# Use an official Python runtime as a parent image
FROM python:3.11-slim

RUN apt-get update -qq \
  && apt-get install -y curl \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /code/

# Collect static files
RUN python3 manage.py collectstatic --noinput

# Start server
# CMD python manage.py migrate && python manage.py makemigrations && gunicorn webSchedule.wsgi:application --bind 0.0.0.0:8000 
