# infrastructure/main.tf

# Proveedor 
provider "aws"{
    region = "us-east-1"
}

# Maquina virtual tipo EC2
resource "aws_instance" "trial_early_warning" {
    ami = "ami-0c55b159cbfafe1f0"
    instance_type = "t3.medium"
    key_name = "mlops-deploy-key"
    tags = {
        Name = "Trial_Early_Warning"
        Environment = "Prod"
        Team = "Data-Science-ArchData"
    }
}