import boto3
import json

def create_role(client):
	sts_role = {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::717063266043:root"
      },
      "Action": "sts:AssumeRole",
      "Condition": {}
    }
  ]
}
	response = client.create_role(Path= "/",
					RoleName = "RSC-MACA-SHARED-OPS-PRD",
					AssumeRolePolicyDocument=json.dumps(sts_role))
	role_name = response["Role"]["RoleName"]
	return role_name

def role_policy(client,role_name):
	response = client.attach_role_policy(
    RoleName=role_name,
    PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess'
)

def main():
	client = boto3.client('iam')
	role_name = create_role(client)
	role_policy(client,role_name)
main()
