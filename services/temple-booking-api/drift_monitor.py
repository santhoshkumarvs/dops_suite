from alibi_detect.cd import MMDDrift
from prometheus_client import start_http_server, Gauge
import numpy as np
import joblib
import time

# Load baseline data & model
X_ref = np.load("data/baseline.npy")  # pre-collected reference data
model = joblib.load("models/your_model.pkl")

drift_detector = MMDDrift(X_ref, p_val=0.05)

# Prometheus metric
drift_score_gauge = Gauge('drift_score', 'Drift score from Alibi Detect')

def run_monitoring():
    start_http_server(8000)  # Prometheus scrapes here

    while True:
        # Simulate new data input
        X_new = np.random.rand(100, X_ref.shape[1])  # replace with actual data input

        preds = drift_detector.predict(X_new)
        drift_score = preds['data']['p_val']

        print(f"Drift score: {drift_score}")
        drift_score_gauge.set(drift_score)

        time.sleep(60)  # Every minute

if __name__ == "__main__":
    run_monitoring()
