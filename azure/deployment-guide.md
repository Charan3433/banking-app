# Azure Deployment Guide

## Azure VM
- Provision a Linux VM in the banking resource group.
- Install Docker and Docker Compose.
- Clone the repository and run `docker compose up --build`.

## Application Gateway
- Place the VM behind an Application Gateway for TLS termination and routing.
- Configure health probes to `/api/health`.

## Load Balancer
- Use Azure Load Balancer for distributing traffic across multiple backend VMs.

## Firewall
- Restrict inbound traffic to required ports only.
- Allow HTTPS, SSH, and application-specific ports.

## Bastion
- Use Azure Bastion for secure VM administration.

## Monitor and Log Analytics
- Enable Azure Monitor and Log Analytics for container/runtime visibility.
- Collect application logs, health metrics, and infrastructure metrics.
