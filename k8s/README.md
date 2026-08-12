# AKS Deployment Guide

This folder contains Kubernetes manifests for deploying the banking app to AKS.

## Image names
Build and push two images to ACR:
- `backend`: `REPLACE_WITH_ACR_LOGIN_SERVER/banking-backend:latest`
- `frontend`: `REPLACE_WITH_ACR_LOGIN_SERVER/banking-frontend:latest`

## Create backend secrets
After AKS is ready, create Kubernetes secrets using the values from Terraform outputs:

```bash
kubectl create secret generic banking-backend-secrets \
  --from-literal=DATABASE_URL="<DATABASE_URL>" \
  --from-literal=SECRET_KEY="<SECRET_KEY>" \
  --from-literal=JWT_ALGORITHM="HS256" \
  --from-literal=JWT_EXPIRATION_HOURS="8" \
  --from-literal=CORS_ORIGINS="*"
```

## Deploy the application

```bash
kubectl apply -f k8s/backend-service.yaml
kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/frontend-service.yaml
kubectl apply -f k8s/frontend-deployment.yaml
```

## Get public IP

```bash
kubectl get svc banking-frontend
```

Access the app at the external IP shown by the frontend LoadBalancer service.
