terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}
variable "access_key" {
  description = "AWS IAM access key"
  type        = string
  sensitive   = true
}
variable "secret_key" {
  description = "AWS IAM secret key"
  type        = string
  sensitive   = true
}
provider "aws" {
  region     = "us-east-1"
  access_key = var.access_key
  secret_key = var.secret_key
}

resource "aws_s3_bucket" "create-my-bucket" {
  bucket = "some-bucket-name-that-must-be-globally-unique"
}