import boto3
from botocore.exceptions import ClientError

regions = ["us-east-1","us-west-2","eu-central-1"]
for region in regions:
	client = boto3.client('s3',region_name='us-west-2')
	bucket_list = client.list_buckets()
	for bucket_name in bucket_list['Buckets']:
		try:
			encrp_status = client.get_bucket_encryption(Bucket=bucket_name['Name'])
			for Algorithm_details in encrp_status['ServerSideEncryptionConfiguration']['Rules']:
				print (bucket_name['Name'] +' '+ Algorithm_details['ApplyServerSideEncryptionByDefault']['SSEAlgorithm'])
		except ClientError:
			print(bucket_name['Name'] +' '+ 'Not encrypted' )