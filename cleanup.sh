#!/bin/bash
echo "🚨 Cleaning up local infra..."
k3d cluster delete dharma-cluster
cd infrastructure/terraform && terraform destroy -auto-approve
