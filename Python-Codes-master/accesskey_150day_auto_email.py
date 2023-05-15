import boto3
from datetime import date, datetime, timedelta,timezone
from datetime import date
import csv
import os
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

roles = ["arn:aws:iam::070992492667:role/ROLE-ADM"]

def accesskey_150(session,writer,account):
	usr_details = {}
	client = session.client('iam')
	list_user = client.list_users()
	for user_name in list_user['Users']:
		describe_accesskey = client.list_access_keys(UserName=user_name['UserName'])
		for accesskey_createddate in describe_accesskey['AccessKeyMetadata']:
			current_date = datetime.now(timezone.utc)
			age = (current_date-accesskey_createddate['CreateDate']).days
			if age >= 10:
				usr_details['Account_ID'] = account[4]
				usr_details['USERNAME'] = accesskey_createddate['UserName']
				usr_details['CREATED_DAYS_AGO'] = age
				usr_details['CURRENT_ACCESSKEY'] = accesskey_createddate['AccessKeyId']
				writer.writerow(usr_details)

def send_mail_to_user(file_name):
    client = boto3.client('ses',"us-west-2")
    file = MIMEMultipart('mixed')
    msg = MIMEApplication(open(file_name, 'r').read())
    msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_name))
    file.attach(msg)
    send_mail = client.send_raw_email(Source="rss-support-d@8kmiles.com",Destinations = ["rss-support-d@8kmiles.com"],RawMessage ={"Data": file.as_string(),})
    print ("")


def main():
	sts_client = boto3.client("sts")
	fieldnames = ["Account_ID","USERNAME","CREATED_DAYS_AGO","CURRENT_ACCESSKEY"]
	file_name = "usr_details.csv"
	with open (file_name,"w",newline='') as csv_file:
		writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
		writer.writeheader()
		for role_arn in roles:
		    sts_response = sts_client.assume_role(RoleArn = role_arn,RoleSessionName = "awstoaws")
		    session = boto3.Session(
		    aws_access_key_id = (sts_response["Credentials"]["AccessKeyId"]),
		    aws_secret_access_key = (sts_response["Credentials"]["SecretAccessKey"]),
		    aws_session_token = (sts_response["Credentials"]["SessionToken"]))
		    account = role_arn.split(":")
		    accesskey_150(session,writer,account)
	send_mail_to_user(file_name)

main()




		
		