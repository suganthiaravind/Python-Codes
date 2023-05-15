import boto3

def role_duration(Role_name):
    client = boto3.client('iam')
    try:
        response = client.update_role(RoleName=Role_name,MaxSessionDuration=43200)
        print ("STS Duration changed to 12hrs to role name ", Role_name)
    
    except:
        print ("Unable to change STS duration Role",IAM_Role_names)
    


def lambda_handler(event, context):

    Role_name = event['detail']['responseElements']['role']['roleName']
    role_duration(Role_name)