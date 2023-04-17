# Dockerfile for Falcon app

# Backend
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

# Expose port 8000 for the Falcon app
EXPOSE 8080
CMD ["python", "app.py"]

# Frontend
# Copy the index.html file to the container
COPY index.html /app

EXPOSE 80
