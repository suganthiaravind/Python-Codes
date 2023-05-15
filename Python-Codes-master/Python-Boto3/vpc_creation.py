import boto3

client = boto3.client('ec2', region_name="us-east-1", aws_access_key_id="AKIAZOUVZGPAYOR2WWAR", aws_secret_access_key="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")

print ("Enter the CIDR value for VPC: ")
vpc_cidr_input = input()
create_vpc_var = client.create_vpc(CidrBlock=vpc_cidr_input)
vpc_ID = create_vpc_var['Vpc']['VpcId']
print ("The VPC ID is: ", vpc_ID)
print ("===================================")

print ("Enter the CIDR value for Subnet: ")
subnet_cidr_input = input()
create_subnet_var = client.create_subnet(VpcId=vpc_ID, CidrBlock=subnet_cidr_input)
subnet_ID = create_subnet_var['Subnet']['SubnetId']
print ("The SUBNET ID is: ", subnet_ID)
print ("===================================")

Create_IGW = client.create_internet_gateway()
igw_ID = Create_IGW['InternetGateway']['InternetGatewayId']
print("The Internet Gateway ID is: ", igw_ID)
print ("===================================")

Attach_IGW = client.attach_internet_gateway(InternetGatewayId=igw_ID,VpcId=vpc_ID)
print ("Internet Gateway Successfull Attached")
print ("===================================")


