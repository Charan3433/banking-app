# Enterprise Architecture Overview

## Components
- Frontend: React 19 + Vite + React Router + Material UI
- Backend: Flask REST API with JWT and SQLAlchemy
- Database: SQLite for local development; ready for Azure SQL migration
- Infrastructure: Docker Compose, Nginx, Terraform, Azure deployment docs

## Security
- JWT-based authentication
- Password hashing with bcrypt
- Environment-based secrets and config
- Structured logging and health endpoints

## DevOps Readiness
- GitHub Actions CI workflow
- Docker multi-stage builds
- Azure deployment starter Terraform
- Azure Monitor and Key Vault guidance
