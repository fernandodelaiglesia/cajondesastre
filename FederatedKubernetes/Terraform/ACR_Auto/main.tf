provider "azurerm" {
  features {}
}

#resource "azurerm_resource_group" "rg" {
#  name     = "resourceGroup1"
#  location = "West US"
#}

resource "azurerm_container_registry" "acr" {
  name                     = "fernandocontainerRegistry2"
  resource_group_name      = var.resourcegroup
  location                 = var.location
  sku                      = "Standard"
  admin_enabled            = true
}

