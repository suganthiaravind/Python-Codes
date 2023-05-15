import boto3

client = boto3.client('ec2')
response = client.describe_volumes()
for a in response['Volumes']:
	if a['State'] == 'available':
		print(a['VolumeId'], a['State'])