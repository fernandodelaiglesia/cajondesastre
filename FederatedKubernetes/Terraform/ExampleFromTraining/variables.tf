variable "region" {
  type    = string
  default = "eu-central-1" # Frankfurt
}

variable "ami" {
  description = "AMI of image"
  default     = "ami-0e8286b71b81c3cc1" # Official CentOS in eu-central-1 "ami-0c3f128b7298d29b9" eu-west-2 Ubuntu-18.04
}

variable "instance_type" {
  description = "EC2 instance type"
  default     = "t2.micro"
}

variable "project_tags" {
  description = "Project tags to be used to track costs."
  type        = map(string)
  default = {
    Name       = "Instancia"
    Owner      = "Fernando de la Iglesia"
    Purpose    = "Testing"
    CostCenter = "Thor"
  }
}

variable "key_name" {
  type    = string
  default = "fernando.delaiglesia.AWS"
}
