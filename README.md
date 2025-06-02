# dops_suite
# dops_suite

A unified, three-tier DharmaConnect platform integrating:

- MLOps (Model Training, Drift, Auto-Retrain)
- FinOps (Cloud Cost Control + Transparency)
- AIOps (Automated Ops and Monitoring)
- LLMOps (LangChain, Feedback Loops)
- EdgeOps (Local Deployment for Temples and Regions)

Built for Bharat. Aligned with Sanatana values.


dops_suite/
├── .github/
│   └── workflows/
│       └── ci-cd.yml                # GitHub Actions workflow
├── infrastructure/
│   ├── terraform/
│   │   └── main.tf                  # Placeholder
│   └── helm-charts/
│       └── temple-service/          # Chart for one service
├── k8s-manifests/
│   ├── base/
│   │   └── deployment.yaml
│   └── overlays/
│       ├── dev/
│       └── prod/
├── mlops/
│   ├── models/
│   ├── training/
│   │   └── train.py
│   ├── drift-detection/
│   │   └── detect_drift.py
│   └── pipelines/
│       └── airflow_pipeline.py
├── llmops/
│   ├── langchain-apps/
│   ├── rag-backend/
│   │   └── vector_store.py
│   └── feedback-loop/
│       └── rlaif_trainer.py
├── aiops/
│   └── monitoring/
│       ├── prometheus.yml
│       └── grafana-dashboards/
├── finops/
│   └── dashboards/
│       └── kubecost.json
├── edgeops/
│   └── k3s-deployments/
│       └── pooja-delivery-k3s.yaml
├── services/
│   ├── temple-booking-api/
│   │   └── main.py
│   ├── pooja-delivery-api/
│   ├── devotional-content/
│   └── cab-booking/
├── frontend/
│   ├── web-app/
│   │   └── pages/
│   └── mobile-app/
│       └── main.dart
├── docs/
│   └── architecture/
│       └── dops_architecture.md
├── scripts/
│   └── bootstrap.sh
├── tests/
│   └── integration-tests/
├── LICENSE
├── README.md
└── .gitignore
