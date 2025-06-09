from flask import Flask
from prometheus_client import generate_latest, Counter, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Define a simple Prometheus counter
REQUEST_COUNT = Counter('finsight_api_requests_total', 'Total API Requests')

@app.route('/')
def index():
    REQUEST_COUNT.inc()
    return "Hello from FinSight API"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
