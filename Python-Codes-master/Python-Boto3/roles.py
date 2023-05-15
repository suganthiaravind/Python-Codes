import boto3 

def roles_fun(session1):

	client = session1.client('iam')
	list_role_var = client.list_roles()
	for i in list_role_var['Roles']:
		IAM_Role_names = i['RoleName']
		
		if (IAM_Role_names.startswith("ROLE-PDAA-ANALYTICSDATA")):
			try:		
				response = client.update_role(RoleName=IAM_Role_names,MaxSessionDuration=43200)
				print ("STS Duration changed to 12hrs to role name ",IAM_Role_names)
			except:
				print ("Unable to change STS duration Role",IAM_Role_names)

		elif (IAM_Role_names.startswith("ROLE-PDAA-DATASCIENCE")):
			try:
				print ("STS Duration changed to 12hrs to role name ",IAM_Role_names)
			except:
				print ("Unable to change STS duration Role",IAM_Role_names)

def OtherAccountAccess(session):
    # Give the PDAA Account number
    PDAA_Accnt_No = [
    "275215173357",
    "647027417980",
    "101928547574",
    "739612272867",
    "836183546189", 
    "853547747509",
    "361044031783",
    "059071749588",
    "715846244538",
    "686943464330",
    "905165670416", 
    "799730443770",
    "040759221257",
    "401177800045",
    "787141626624",
    "929901035033"]

    for account_number in PDAA_Accnt_No:
        sts_client = session.client("sts")
        role_arn = "arn:aws:iam::"+account_number+":role/OrganizationAccountAccessRole"
        sts_response = sts_client.assume_role(RoleArn = role_arn,RoleSessionName = "awstoaws") # Creating second session
        session1 = boto3.Session(
        aws_access_key_id = (sts_response["Credentials"]["AccessKeyId"]),
        aws_secret_access_key = (sts_response["Credentials"]["SecretAccessKey"]),
        aws_session_token = (sts_response["Credentials"]["SessionToken"]))
        roles_fun(session1)

if __name__ == '__main__':
    sts_client = boto3.client("sts")
    sts_response = sts_client.assume_role(RoleArn = "arn:aws:iam::057541488235:role/ROLE-SHARED-PRD-CROSSACCOUNT",RoleSessionName = "awstoaws")
    session = boto3.Session(
    aws_access_key_id = (sts_response["Credentials"]["AccessKeyId"]),
    aws_secret_access_key = (sts_response["Credentials"]["SecretAccessKey"]),
    aws_session_token = (sts_response["Credentials"]["SessionToken"]))
    OtherAccountAccess(session)
