import boto3

client = boto3.client('s3',aws_access_key_id="AKIAZOUVZGPA", aws_secret_access_key="Nzxe6MiCST+q8glWPcInLt")

s3_response = client.list_buckets()

for i in s3_response['Buckets']:
	Created_date = i['CreationDate']
	bucket_name = i['Name']

	s3_Location_response = client.get_bucket_location(Bucket=bucket_name)
	print (bucket_name, s3_Location_response['LocationConstraint'])
