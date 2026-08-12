variable "subscription_id" {
  type = string
}

variable "resource_group_name" {
  type    = string
  default = "charannewaks-rg"
}

variable "location" {
  type    = string
  default = "eastus"
}

variable "aks_cluster_name" {
  type    = string
  default = "charannewaks-aks"
}

variable "acr_name" {
  type    = string
  default = "charannewaks"
}

variable "postgres_server_name" {
  type    = string
  default = "charannewaks-db"
}

variable "postgres_admin_username" {
  type    = string
  default = "bankingadmin"
}

variable "postgres_database_name" {
  type    = string
  default = "bankingdb"
}

variable "postgres_version" {
  type    = string
  default = "15"
}
