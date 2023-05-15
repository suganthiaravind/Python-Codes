import boto3
from datetime import date, datetime, timedelta,timezone
from datetime import date
import csv
import os
from botocore.exceptions import ClientError
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

roles = ["arn:aws:iam::034930744685:role/assumerole-102336539363"]

def accesskey_150(session,writer):
	usr_details = {}
	client = session.client('iam')
	list_user = client.list_users()
	for user_name in list_user['Users']:
		describe_accesskey = client.list_access_keys(UserName=user_name['UserName'])
		for accesskey_createddate in describe_accesskey['AccessKeyMetadata']:
			current_date = datetime.now(timezone.utc)
			age = (current_date-accesskey_createddate['CreateDate']).days
			if age >= 0:
				usr_details['USERNAME'] = accesskey_createddate['UserName']
				usr_details['CREATED_DAYS_AGO'] = age
				usr_details['CURRENT_ACCESSKEY'] = accesskey_createddate['AccessKeyId']
				writer.writerow(usr_details)

def send_mail_to_user(file_name):
	SENDER = "hitechmay2020@gmail.com"
	RECIPIENT = "hitechmay2020@gmail.com"
	SUBJECT = "Accesskey 150 Age Data"
	ATTACHMENT = file_name
	BODY_HTML = """\
	<html>
	<head></head>
	<body>
	<h3>Hi All</h3>
	<p>Please see the attached file for a list of Accesskey those are created 150days ago.</p>
	</body>
	</html>
	"""
	CHARSET = "utf-8"
	client = boto3.client('ses')
	msg = MIMEMultipart('mixed')
	msg['Subject'] = SUBJECT 
	msg['From'] = SENDER 
	msg['To'] = RECIPIENT
	
	msg_body = MIMEMultipart('alternative')
	htmlpart = MIMEText(BODY_HTML.encode(CHARSET), 'html', CHARSET)
	msg_body.attach(htmlpart)
	att = MIMEApplication(open(ATTACHMENT, 'rb').read())
	att.add_header('Content-Disposition','attachment',filename=os.path.basename(ATTACHMENT))
	msg.attach(msg_body)
	msg.attach(att)
	try:
	    response = client.send_raw_email(
	        Source=SENDER,
	        Destinations=[
	            RECIPIENT
	        ],
	        RawMessage={
	            'Data':msg.as_string(),
	        }
	    ) 
	except ClientError as e:
	    print(e.response['Error']['Message'])
	else:
	    print("Email sent! Message ID:"),
	    print(response['MessageId'])

def lambda_handler(event, context):
	sts_client = boto3.client("sts")
	fieldnames = ["USERNAME","CREATED_DAYS_AGO","CURRENT_ACCESSKEY"]
	file_name = "/tmp/usr_details.csv"
	with open (file_name,"w",newline='') as csv_file:
		writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
		writer.writeheader()
		for role_arn in roles:
		    sts_response = sts_client.assume_role(RoleArn = role_arn,RoleSessionName = "awstoaws")
		    session = boto3.Session(
		    aws_access_key_id = (sts_response["Credentials"]["AccessKeyId"]),
		    aws_secret_access_key = (sts_response["Credentials"]["SecretAccessKey"]),
		    aws_session_token = (sts_response["Credentials"]["SessionToken"]))
		    accesskey_150(session,writer)
	send_mail_to_user(file_name)