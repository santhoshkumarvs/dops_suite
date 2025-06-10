from prometheus_client import start_http_server, Counter
import time
from fastapi import FastAPI

app = FastAPI()

REQUEST_COUNT = Counter("finsight_requests_total", "Total number of requests")

@app.get("/")
def read_root():
    REQUEST_COUNT.inc()
    return {"message": "Hello from FinSight API"}

# Expose Prometheus metrics
start_http_server(8001)  # Exposes on separate port from FastAPI

