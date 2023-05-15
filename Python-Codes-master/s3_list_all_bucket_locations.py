import boto3
import csv 

def OtherAccountAccess(session,writer):
    #Give the shared prd dynamodb tabe values based on your work nature.
	table_names = ["DYNAMODB-RSC-PHC-PRD-ACCOUNT-NUMBER"]
	db_client  = boto3.client('dynamodb',region_name='us-west-2')
	for table_name in table_names:
		response = db_client.scan(TableName=table_name)
		for arn in response['Items']:
			account_number = arn['AccountNumber']['S']
			sts_client = session.client("sts")
			role_arn = "arn:aws:iam::"+account_number+":role/OrganizationAccountAccessRole"
			sts_response = sts_client.assume_role(RoleArn = role_arn,RoleSessionName = "awstoaws") # Creating second session
			session1 = boto3.Session(
			aws_access_key_id = (sts_response["Credentials"]["AccessKeyId"]),
			aws_secret_access_key = (sts_response["Credentials"]["SecretAccessKey"]),
			aws_session_token = (sts_response["Credentials"]["SessionToken"]))
			bkt_fun(session1,writer,account_number)


def bkt_fun(session1,writer,account_number):
	bkt_dict = {}
	client = session1.client('s3')

	print("Running on"+ account_number)

	list_bkt = client.list_buckets()
	for bkt_name in list_bkt['Buckets']:
		
		try:
			bkt_location = client.get_bucket_location(Bucket=bkt_name['Name'])
			
			bkt_dict["Account_ID"] = account_number
			bkt_dict["Bucket_Name"] = bkt_name['Name']
			bkt_dict["Locations"] = bkt_location['LocationConstraint']
			writer.writerow(bkt_dict)

		except Exception as e:
			print (e)
		

def main():
	sts_client = boto3.client("sts")
	fieldnames = ["Account_ID","Bucket_Name","Locations"]
	file_name = "bkt_dict.csv"
	with open (file_name,"w",newline='') as csv_file:
		writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
		writer.writeheader()
		sts_client = boto3.client("sts")
		sts_response = sts_client.assume_role(RoleArn = "arn:aws:iam::057541488235:role/ROLE-SHARED-PRD-CROSSACCOUNT",RoleSessionName = "awstoaws")
		session = boto3.Session(
		aws_access_key_id = (sts_response["Credentials"]["AccessKeyId"]),
		aws_secret_access_key = (sts_response["Credentials"]["SecretAccessKey"]),
		aws_session_token = (sts_response["Credentials"]["SessionToken"]))
		OtherAccountAccess(session,writer)
main()