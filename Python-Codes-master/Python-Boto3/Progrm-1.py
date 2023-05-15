# IAM users List

import boto3 

client = boto3.client('iam', aws_access_key_id="AKIAZOUVZGPAYOR2WWAR", aws_secret_access_key="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")

var_lst_usr = client.list_users()

for xyz in var_lst_usr['Users']:
	print (xyz['CreateDate'], xyz['UserName'])
