# Banking Application

A production-style banking web application built with React, Flask, SQLAlchemy, Docker, and Azure-ready deployment structure.

## Architecture

- Frontend: React 19 + Vite + Material UI
- Backend: Flask + SQLAlchemy + JWT + Flask-Migrate
- Database: SQLite for local development
- Containerization: Docker Compose
- DevOps: GitHub Actions, Terraform, Azure deployment docs

## Folder Structure

- frontend/ - React frontend application
- backend/ - Flask API and business logic
- database/ - database scripts and migrations
- docker/ - Docker-related assets
- terraform/ - Azure infrastructure starter code
- azure/ - deployment documentation
- nginx/ - reverse proxy configuration
- docs/ - project documentation

## Running Locally

1. Copy .env.example to .env
2. Run `docker compose up --build`
3. Open http://localhost:3000

## API Endpoints

- POST /api/auth/register
- POST /api/auth/login
- POST /api/auth/forgot-password
- GET /api/users/profile
- PUT /api/users/profile
- GET /api/accounts
- POST /api/accounts
- GET /api/transactions
- POST /api/transactions/deposit
- POST /api/transactions/withdraw
- GET /api/health

## Docker Commands

- `docker compose build`
- `docker compose up`
- `docker compose down`

## Azure Deployment Notes

The project includes starter Terraform and Azure deployment documentation under terraform/ and azure/ for future deployments to Azure VM, Application Gateway, Firewall, Load Balancer, Monitor, Key Vault, and Azure SQL.
