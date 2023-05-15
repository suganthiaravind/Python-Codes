import boto3
ec2 = boto3.resource('ec2',region_name='us-west-2')

instances = ec2.create_instances(
	ImageId='ami-01dcb3e8389cdf2ef',
	 
	MinCount=1,
	MaxCount=1,
	InstanceType='t2.micro',
	SubnetId='subnet-08b626ce43d198704',
	SecurityGroupIds=['sg-068a14629e871357e'],
	KeyName='rsc-uat'	
 )