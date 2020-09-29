provider "aws" {
    region = "eu-west-2"
}

resource "aws_iam_user" "MyAWSResource" {
    name  = "ArvindPulijala"
}

output "output" {
  description = "CIDR Values"
  value = formatlist("%s/32", var.grey_build_agent_pips)

}


variable "grey_build_agent_pips" {
    default = [ "18.132.141.180/32",
                "18.132.62.157/32",
                "18.132.117.246/32"
            ]
}
