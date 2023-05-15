import boto3

client = boto3.client('iam')
response = client.list_roles()
for x in response['Roles']:
        print (x['RoleName'])
