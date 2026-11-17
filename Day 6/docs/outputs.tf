
output "aws_account_id" {
  description = "Current AWS account ID"
  value       = data.aws_caller_identity.current.account_id
}

output "aws_user_arn" {
  description = "Current AWS identity ARN"
  value       = data.aws_caller_identity.current.arn
}


