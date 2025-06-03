FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#CMD ["python", "main.py"]
# Install Prometheus client and Alibi Detect
RUN pip install alibi-detect prometheus-client

# Copy and run the drift monitor
COPY drift_monitor.py /app/drift_monitor.py

# Run both the API and drift monitor (use a process manager or simple script)
CMD ["sh", "-c", "python drift_monitor.py & uvicorn main:app --host 0.0.0.0 --port 80"]
