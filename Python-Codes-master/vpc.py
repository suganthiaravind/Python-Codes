import boto3
client = boto3.client('ec2')
data1 = client.create_vpc(
    CidrBlock='10.211.0.0/16',
    AmazonProvidedIpv6CidrBlock=False,
    InstanceTenancy='default'
)

vpc_id = data1["Vpc"]["VpcId"]
print vpc_id
