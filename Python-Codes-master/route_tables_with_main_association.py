import boto3
ec2 = boto3.resource('ec2')
route_tables_with_main_association = ec2.route_tables.filter(
    Filters=[{'Name': 'vpc-id', 'Values': ["vpc-065caefdd83f61289"]}])
 
for t in route_tables_with_main_association:
    print(t.id)
