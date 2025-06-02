# dops_suite

**A comprehensive DevOps, MLOps, AIOps, FinOps, LLMOps unified project suite**  
Designed to power the DharmaConnect ecosystem with best-in-class practices for scalable, secure, and production-grade cloud native applications.

---

## Overview

dops_suite is a modular monorepo that integrates multiple operational domains:

- **AI Ops**: Monitoring, alerting, Grafana dashboards  
- **ML Ops**: Data pipelines, training, model store, drift detection, retraining  
- **LLM Ops**: Langchain apps, RAG backend, feedback loops, prompt management  
- **Fin Ops**: Cost dashboards and cloud resource optimization  
- **Edge Ops**: Lightweight k3s Kubernetes deployments  
- **Infrastructure**: Terraform and Helm charts for reproducible infra-as-code  
- **Deployments**: Kubernetes manifests with overlays for dev/prod  
- **Services**: Microservices for temple booking, pooja delivery, devotional content, cab booking  
- **Frontend**: Web and mobile apps for user interaction  
- **Testing**: Unit, integration, and end-to-end tests  
- **Documentation**: Architecture and process docs

---

## Getting Started

### Prerequisites

- Docker & Docker Compose  
- Kubernetes CLI (kubectl)  
- Helm 3  
- Terraform  
- Python 3.9+ (for ML and backend services)  
- Node.js 16+ (for frontend apps)

### Setup

1. Clone the repo  
   ```bash
   git clone https://github.com/santhoshkumarvs/dops_suite.git
   cd dops_suite
