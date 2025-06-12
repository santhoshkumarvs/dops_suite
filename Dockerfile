# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy app.py into the container
COPY app.py .

# Install required packages
RUN pip install flask prometheus_client

# Expose port 8000
EXPOSE 8000

# Run the app
CMD ["python", "app.py"]
