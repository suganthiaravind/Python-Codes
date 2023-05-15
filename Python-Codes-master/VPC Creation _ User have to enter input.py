import boto3
ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

print "******VPC Creation******"
vpcinput = raw_input("Enter the valid CIDR: ")

create_vpc = client.create_vpc(

    CidrBlock=vpcinput,

)
vpcid = create_vpc['Vpc']['VpcId']
print 'VPC ID is', vpcid

print "==================================================================="

print '******Subnet Creation******'
print 'VPC CIDR: ', vpcinput
subnetinput = raw_input("Enter the valid subnet CIDR: ")

available_zones = ["us-west-2a", "us-west-2b", "us-west-2c", "us-west-2d"]
print(available_zones)

availability_zone = raw_input("Select any one AZ from above list: ")

create_subnet = client.create_subnet(
    AvailabilityZone=availability_zone,
    CidrBlock=subnetinput,
    VpcId=vpcid,
)

subnetid = create_subnet['Subnet']['SubnetId']
print subnetid


print "==================================================================="
print '******Internet Gateway Creation******'

ig_create = client.create_internet_gateway()
ig_id = ig_create["InternetGateway"]["InternetGatewayId"]
print 'Internet Gateway ID is', ig_id

print "==================================================================="
print '******Internet Gateway Attaching to VPC******'

response = client.attach_internet_gateway(
    InternetGatewayId = ig_id,
    VpcId = vpcid
)
print "Internet Gateway Attached successfully"

print "==================================================================="
print '******Route Table Entries******'

route_tables_with_main_association = ec2.route_tables.filter(
    Filters=[{'Name': 'vpc-id', 'Values': [vpcid]}])
for t in route_tables_with_main_association:
    print(t.id)

subnet_associate = client.associate_route_table(
    RouteTableId=t.id,
    SubnetId=subnetid
)
print "subnet successfully associated"

response = client.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=ig_id,
    RouteTableId=t.id,
)

print "Routing enter has been added"


print "================================================================="
print "================================================================="
print "******************************************************************"
print 'VPC ID is', vpcid
print 'Subnet ID is', subnetid
print 'Internet Gateway ID is', ig_id
print "******************************************************************"







