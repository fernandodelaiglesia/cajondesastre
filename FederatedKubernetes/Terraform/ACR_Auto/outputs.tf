
output "login_name" {
  description = "Login que hay que usar."
  value       = azurerm_container_registry.acr.admin_username
}

output "login_pass" {
  description = "Pass del Login que hay que usar."
  value       = azurerm_container_registry.acr.admin_password
}

