# Use official Python image as base
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code to the container
COPY . /app

# Expose port 5000 for Flask
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=run.py
ENV FLASK_DEBUG=1

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]
