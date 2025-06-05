from alibi_detect.cd import MMDDrift
import numpy as np
import joblib
import prometheus_client

reference_data = np.load("ref_data.npy")
model = MMDDrift(reference_data, p_val=.05)

def detect_drift(new_data):
    preds = model.predict(new_data)
    score = preds['data']['p_val']
    prometheus_client.Gauge('model_drift_score', 'Drift score').set(score)
    if score < 0.05:
        print("Drift detected! Triggering retrain...")
        retrain_model()
    return score

def retrain_model():
    # Dummy retrain logic — replace with real
    print("Retraining model...")
    # Save new reference
    joblib.dump(model, "models/drift_model.joblib")
