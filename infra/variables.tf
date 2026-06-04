variable "location" {
  default = "eastus"
}

variable "vm_size" {
  default = "Standard_D2s_v3"
}

variable "admin_username" {
  default = "azureuser"
}

variable "public_key" {
  type = string
}