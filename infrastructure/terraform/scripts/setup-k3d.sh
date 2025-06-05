#!/bin/bash

echo "🚀 Creating k3d cluster..."
k3d cluster create dharma-cluster --config cluster-config.yaml

echo "✅ Initializing Terraform..."
cd infrastructure/terraform
terraform init && terraform apply -auto-approve

echo "🛡️ Cluster and Terraform infra ready."
