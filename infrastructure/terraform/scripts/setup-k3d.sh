#!/bin/bash

set -e

CLUSTER_NAME="dharma-connect-cluster"

# Check if cluster already exists
if k3d cluster list | grep -q "$CLUSTER_NAME"; then
  echo "✅ K3d cluster '$CLUSTER_NAME' already exists. Skipping creation."
else
  echo "🚀 Creating new k3d cluster: $CLUSTER_NAME"
  k3d cluster create "$CLUSTER_NAME" --servers 1 --agents 2 -p "8080:80@loadbalancer" -p "443:443@loadbalancer"
  echo "✅ K3d cluster '$CLUSTER_NAME' created."
fi

# Show cluster status
kubectl get nodes
