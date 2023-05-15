import boto3
client = boto3.client('ec2', region_name = 'us-east-1')
response = client.describe_regions(Filters=[{'Name': 'region-name', 'Values': ['us-east-1', 'eu-central-1', 'us-west-2']}])
for Region in response['Regions']:
    ec2client = boto3.client('ec2', region_name=Region['RegionName'])
    response1 = ec2client.describe_images(Owners=['self'])
    AMI_Images = response1['Images']
    for images in AMI_Images:
        Image_ID = (images['ImageId'])
        Tag_Values = images['Tags']
        for tag in Tag_Values:
            response3 = ec2client.create_tags(
                Resources=[Image_ID],
                Tags=[
                    {
                        'Key': 'Owner',
                        'Value': 'rsc'
                    },
                    {
                        'Key': 'Environment',
                        'Value': 'sandbox'
                    },
                    {
                        'Key': 'CostCenter',
                        'Value': '0000004752'
                    },
                    {
                        'Key': 'BusinessUnit',
                        'Value': 'gis'
                    },
                    {
                        'Key': 'WBS',
                        'Value': 'i160.33102.02.00.11'
                    },
                ]
            )
