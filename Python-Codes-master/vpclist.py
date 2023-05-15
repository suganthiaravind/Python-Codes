import boto3
vpccre=boto3.client('ec2', region_name='us-west-2')
svcreatvpc=vpccre.describe_vpcs()
vpcs=svcreatvpc['Vpcs']

print vpcs

for x in vpcs:
	for y in x["Tags"]:
		print(y.get("Value"))
