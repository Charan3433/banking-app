# AKS Deployment Steps

1. Initialize Terraform in the `terraform/` folder:
   ```bash
   cd terraform
   terraform init
   terraform apply
   ```

2. Connect to AKS:
   ```bash
   az aks get-credentials --resource-group charannewaks-rg --name charannewaks-aks
   ```

3. Log in to ACR:
   ```bash
   az acr login --name charannewaks
   ```

4. Build and push Docker images:
   ```bash
   az acr build --registry charannewaks --image banking-backend:latest ./backend
   az acr build --registry charannewaks --image banking-frontend:latest ./frontend
   ```

5. Create backend secrets in AKS and deploy manifests:
   - Use Terraform output values for `DATABASE_URL` and `SECRET_KEY`.
   - Create the secret and apply Kubernetes manifests from `k8s/`.

6. Confirm the frontend service external IP:
   ```bash
   kubectl get svc banking-frontend
   ```

7. Access the app via the external IP in your browser.
