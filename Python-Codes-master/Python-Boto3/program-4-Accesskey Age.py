import boto3
from datetime import date, datetime, timedelta,timezone
from datetime import date 

client = boto3.client('iam', aws_access_key_id="AKIAZOUVZGPAYEPVYTMS", aws_secret_access_key="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")

list_user = client.list_users()
for user_name in list_user['Users']:
	
	describe_accesskey = client.list_access_keys(UserName=user_name['UserName'])
	for accesskey_createddate in describe_accesskey['AccessKeyMetadata']:
		#print (accesskey_createddate['UserName'], accesskey_createddate['AccessKeyId'], accesskey_createddate['CreateDate'])

		current_date = datetime.now(timezone.utc)
		
		age = (current_date - accesskey_createddate['CreateDate']).days
		

		if (age>=0):
			print (accesskey_createddate['UserName'])

