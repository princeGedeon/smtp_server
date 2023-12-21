# Use the official Python base image
FROM python:3.9

# Image name & Author
LABEL image_name="friare_website"
LABEL maintainer="Gédéon Prince GUEDJE - guedjegedeon03@gmail.com"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the Docker image
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files to the image
COPY . /app/

# Expose the port that Django runs on
EXPOSE 8025


# We're going to do this once the container is created by ssh into
# RUN python manage.py createsuperuser
