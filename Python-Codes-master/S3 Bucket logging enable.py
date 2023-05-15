import boto3
client = boto3.client("s3")
source_bucket = 'rmg-mehul-training'
target_bucket = 'rmg-tanya-training'

kw_args = {
    'Bucket': source_bucket,
    'ACL': 'private'
}

client.create_bucket(**kw_args)

kw_args = {
'Bucket': 'target_bucket,
'ACL': 'log-delivery-write'
}

client.create_bucket(**kw_args)

kw_args = {
    'Bucket': source_bucket,
    'BucketLoggingStatus': {
        'LoggingEnabled': {
            'TargetBucket': target_bucket,
            'TargetPrefix': 'logs/'
        }
    }
}

client.put_bucket_logging(**kw_args)

response = client.put_bucket_acl(
    ACL= 'log-delivery-write',
    Bucket='string',
)