# FinSight Deployment – Troubleshooting Log (2025-06-08)

## ✅ Fixed Issues
### 1. Helm Chart Repos Timeout
- ❌ Issue: `helm repo update` failed due to proxy settings or unreachable DNS (10.255.255.254)
- ✅ Fix: `unset HTTP_PROXY HTTPS_PROXY http_proxy https_proxy`

### 2. Nginx 404 Not Found
- ❌ Issue: Accessing root via Ingress showed `404 Not Found`
- ✅ Fix: Verified Ingress routing and backend `finsight-api` readiness + redeployed service/pod.

### 3. Docker Build Failed
- ❌ Issue: `Dockerfile not found`, and outdated app path
- ✅ Fix: Created new `Dockerfile` in correct path matching new `app.py`

### 4. pyOpenSSL AttributeError
- ❌ Issue: Python `crypto.py` failed due to `X509_V_FLAG_NOTIFY_POLICY`
- ✅ Fix: Avoided system package uninstall; switched Python env; ensured compatible `cryptography` version

### 5. Git Push Cleanup
- ❌ Issue: Large `.tgz` and Helm files were untracked and cluttering
- ✅ Fix: Clean `.gitignore`, staged only valid Kubernetes and Helm configs, pushed to `dev`

---

## 🧱 Infrastructure Milestones
- [x] k3d cluster running with namespace `finsight`
- [x] FastAPI app responding at `/` with "Hello from FinSight API"
- [x] Prometheus deployed (retry via `helm repo update` after unsetting proxy)
- [x] Ingress + port-forward verified
