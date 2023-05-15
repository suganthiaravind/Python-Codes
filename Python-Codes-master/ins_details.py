import boto3
ec2 = boto3.resource('ec2',region_name="eu-central-1", aws_access_key_id="AKIAVNJWHOQXVZWJINP5",aws_secret_access_key="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")
instance = ec2.create_instances(
    ImageId = 'ami-076431be05aaf8080',
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.micro',
    KeyName = 'linux-server',
    SubnetId = 'subnet-05fe0a68632b9581b')
print (instance)