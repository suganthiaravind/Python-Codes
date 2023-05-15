import boto3
client = boto3.client('ec2')
ec2 = boto3.resource('ec2')

vpc_create = client.create_vpc(
    CidrBlock='10.11.0.0/16',
    AmazonProvidedIpv6CidrBlock=False,
    InstanceTenancy='default'
)

vpc_id = vpc_create["Vpc"]["VpcId"]
print vpc_id


subnet_create = client.create_subnet(
    AvailabilityZone='us-west-2b',
    CidrBlock = '10.11.1.0/24',
    VpcId = vpc_id,
)

subnet_id = subnet_create["Subnet"]["SubnetId"]
print subnet_id


ig_create = client.create_internet_gateway()
ig_id = ig_create["InternetGateway"]["InternetGatewayId"]
print ig_id

response = client.attach_internet_gateway(
    InternetGatewayId = ig_id,
    VpcId = vpc_id,
)
print "Internet Gateway Attached successfully"


route_tables_with_main_association = ec2.route_tables.filter(
    Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
for t in route_tables_with_main_association:
    print(t.id)


subnet_associate = client.associate_route_table(
    RouteTableId=t.id,
    SubnetId=subnet_id
)
print "subnet successfully associated"

response = client.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=ig_id,
    RouteTableId=t.id,
)

print "Routing enter has been added"
