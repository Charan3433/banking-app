output "acr_login_server" {
  value = azurerm_container_registry.acr.login_server
}

output "aks_cluster_name" {
  value = azurerm_kubernetes_cluster.aks.name
}

output "aks_resource_group" {
  value = azurerm_resource_group.rg.name
}

output "aks_fqdn" {
  value = azurerm_kubernetes_cluster.aks.fqdn
}

output "postgres_fqdn" {
  value = azurerm_postgresql_flexible_server.postgres.fqdn
}

output "database_url" {
  value = local.database_url
}

output "postgres_admin_username" {
  value = var.postgres_admin_username
}

output "postgres_password" {
  value     = random_password.postgres_password.result
  sensitive = true
}

output "secret_key" {
  value     = random_password.secret_key.result
  sensitive = true
}

output "key_vault_uri" {
  value = azurerm_key_vault.kv.vault_uri
}
