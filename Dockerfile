# --- STAGE 1: Build/Install Dependencies ---
# Use an official Python runtime as a parent image
FROM python:3.11-slim AS builder

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# The '--no-cache-dir' flag saves disk space
RUN pip install --no-cache-dir -r requirements.txt

# --- STAGE 2: Final Runtime Image ---
# Use a smaller, cleaner base image for the final application
FROM python:3.11-slim

# Set the working directory for the application
WORKDIR /app

# Copy the installed packages from the 'builder' stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copy the application source code into the container
COPY . .

# Set environment variables (optional but good practice)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Expose the port your application listens on (e.g., 8000 for Django/Flask)
# You can change this to your application's port
EXPOSE 8000

# Command to run the application
# Replace 'your_app.py' or 'gunicorn/uvicorn' command with your actual entry point
CMD ["python", "your_app.py"] 
# Example for a web app: CMD ["gunicorn", "my_project.wsgi:application", "--bind", "0.0.0.0:8000"]