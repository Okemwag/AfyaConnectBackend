FROM python:3.11-alpine
ENV DJ_PORT 8001

# Expose the port your Django app will run on
EXPOSE $DJ_PORT
# Install system dependencies specific to Alpine Linux
RUN apk add --no-cache \
    gcc \
    g++ \
    postgresql-client \
    binutils \
    proj-dev

RUN apk add --no-cache gdal-dev geos-dev

# Set the working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files into the container
COPY . .


CMD python manage.py runserver 0.0.0.0:$DJ_PORT
