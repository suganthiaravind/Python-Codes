import boto3

def generate_csv(data_list,file_name):
    logger.info('generating csv file')
    keys = data_list[0].keys()
    with open(file_name, 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data_list)
    return file_name

regions = ['ap-east-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1', 'eu-central-1', 'eu-north-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'sa-east-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
for region in regions:
    client = boto3.client('ec2',region_name=region)
    response = client.describe_instances()
    data_list = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            data=dict()
            data['instance_id'] = instance["InstanceId"]
            data['private_ip'] = instance["PrivateIpAddress"]
            data['state'] = instance['State']['Name']
        data_list.append(data)
print data_list
generate_csv(data_list,"instance_info.csv")
