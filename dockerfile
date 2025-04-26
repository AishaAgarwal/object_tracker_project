# Use an official lightweight Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file first to leverage Docker cache
COPY requirements.txt .

# Install system dependencies + Python libraries
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

RUN pip install "numpy<2"


# Copy the entire project into the container
COPY . .

# Expose any ports if needed (not necessary for local video processing)
# EXPOSE 8000 

# Run the main file
CMD ["python", "main.py"]
