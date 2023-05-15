import boto3
import csv
roles = ["arn:aws:iam::447249610327:role/ROLE-PHC-CDSE-01-PRD-SS-CROSSACCOUNT",
         "arn:aws:iam::357089579770:role/ROLE-GRED-DEVSCI-OBDDP-01-PRD-SS-CROSSACCOUNT",
         "arn:aws:iam::622716232669:role/ROLE-GRED-DEVSCI-SADP-01-PRD-SS-CROSSACCOUNT",
         "arn:aws:iam::729574509662:role/ROLE-PHC-SHARED-APPS-01-PRD-SS-CROSSACCOUNT",
         "arn:aws:iam::102731293257:role/ROLE-DMZ-PRD-LAMBDA-AD-ROUTE53-S3",
         "arn:aws:iam::637439093730:role/ROLE-RSSBUIT-PRD-LAMBDA-AD-ROUTE53-S3",
         "arn:aws:iam::169925630325:role/ROLE-GISIT-K8S-PRD-LAMBDA-AD-ROUTE53-S3",
         "arn:aws:iam::219042370922:role/ROLE-PHC-RAAD-PRD-01-LAMBDA-AD-ROUTE53-S3",
         "arn:aws:iam::717063266043:role/ROLE-SHARED-PRD-LAMBDA-AD-ROUTE53-S3",
         "arn:aws:iam::624812204564:role/ROLE-PHC-DATASCIENCE-PRD-LAMBDA-AD-ROUTE53-S3",
         "arn:aws:iam::208909166705:role/ROLE-PHC-SHARED-PRD-LAMBDA-AD-ROUTE53-S3",
         "arn:aws:iam::596827342063:role/ROLE-GRED-RPLAT-01-PRD-LAMBDA-AD-ROUTE53-S3",
         "arn:aws:iam::576714887429:role/ROLE-GRED-EHIVE-001-PRD-LAMBDA-AD-ROUTE53-S3",
         "arn:aws:iam::320514908897:role/ROLE-PHC-PRECURATED-DATA-01-PRD-LAMBDA-AD-ROUTE53-S3",
         "arn:aws:iam::812534169699:role/ROLE-PHC-DEVSECOPS-01-PRD-LAMBDA-AD-ROUTE53-S3",
         "arn:aws:iam::267467788804:role/ROLE-PHC-LOGGING-01-PRD-LAMBDA-AD-ROUTE53-S3",
         "arn:aws:iam::030425002777:role/ROLE-GRED-GENEATLAS-01-PRD-LAMBDA-AD-ROUTE53-S3",
         "arn:aws:iam::869484639545:role/ROLE-PHC-CURATED-DATA-01-PRD-LAMBDA-AD-ROUTE53-S3",
         "arn:aws:iam::938131282771:role/ROLE-PHC-QUARANTINE-01-PRD-LAMBDA-AD-ROUTE53-S3",
         "arn:aws:iam::607716346219:role/ROLE-PHC-VISUALIZATION-01-PRD-LAMBDA-AD-ROUTE53-S3",
         "arn:aws:iam::713500322386:role/ROLE-PRED-MASSE-01-PRD-LAMBDA-AD-ROUTE53-S3",
         "arn:aws:iam::438017381278:role/ROLE-DATA-CATALOG-01-PRD-LAMBDA-AD-ROUTE53-S3",
         "arn:aws:iam::694760152192:role/ROLE-PHC-HPC-01-PRD-LAMBDA-AD-ROUTE53-S3",
         "arn:aws:iam::925590726324:role/ROLE-GRED-SCIDB-01-PRD-LAMBDA-AD-ROUTE53-S3",
         "arn:aws:iam::382698428282:role/ROLE-RSS-DETEP-01-SB-SS-CROSSACCOUNT",
        "arn:aws:iam::432573255747:role/ROLE-PTS-ELEAFLET-01-SB-SS-CROSSACCOUNT",
        "arn:aws:iam::908697811128:role/ROLE-PHC-RAAN-SHARED-01-SB-SS-CROSSACCOUNT",
        "arn:aws:iam::028996728432:role/ROLE-PD-SHERLOCK-POC-01-SB-SS-CROSSACCOUNT",
        "arn:aws:iam::325427721242:role/ROLE-PHC-RAAN-VISUALIZATION-01-SB-SS-CROSSACCOUNT",
        "arn:aws:iam::234911921950:role/ROLE-PHC-RAAN-QUARANTINE-01-SB-SS-CROSSACCOUNT",
        "arn:aws:iam::159896904386:role/ROLE-PHC-RAAN-PRECURATED-01-SB-SS-CROSSACCOUNT",
        "arn:aws:iam::151571826708:role/ROLE-PHC-RAAN-CURATED-01-SB-SS-CROSSACCOUNT",
        "arn:aws:iam::426035548931:role/ROLE-PRED-DS-AUTOML-01-SB-SS-CROSSACCOUNT",
        "arn:aws:iam::157682772569:role/ROLE-PTI-TETRASCIENCEDL-POC-01-SB-SS-CROSSACCOUNT",
        "arn:aws:iam::134886565025:role/ROLE-PHC-SHARED-APPS-01-UAT-SS-CROSSACCOUNT",
        "arn:aws:iam::992131851202:role/ROLE-PHC-SHARED-APPS-01-DEV-SS-CROSSACCOUNT",
        "arn:aws:iam::672531519416:role/ROLE-PHC-SHARED-APPS-01-SB-SS-CROSSACCOUNT",
        "arn:aws:iam::828399534975:role/ROLE-GRED-NLP-01-SB-SS-CROSSACCOUNT",
        "arn:aws:iam::848473474001:role/ROLE-PHC-RAAN-AA-01-DEV-SS-CROSSACCOUNT",
        "arn:aws:iam::065794817977:role/ROLE-PHC-RAAN-AI-01-DEV-SS-CROSSACCOUNT",
        "arn:aws:iam::070992492667:role/ROLE-PDIX-PULSAR-01-SB-SS-CROSSACCOUNT",
        "arn:aws:iam::789674631670:role/ROLE-PHC-CDSE-01-DEV-SS-CROSSACCOUNT",
        "arn:aws:iam::383488466047:role/ROLE-PHC-CDSE-01-UAT-SS-CROSSACCOUNT",
        "arn:aws:iam::451655153572:role/ROLE-PRED-CLOUDP-SANDBOX-01-SB-SS-CROSSACCOUNT",
        "arn:aws:iam::336734000948:role/ROLE-PHC-PRECURATED-DATA-01-UAT-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::973907027419:role/ROLE-PHC-POC-SB-05-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::500884129511:role/ROLE-RSSBUIT-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::293144281991:role/ROLE-GRED-FE-01-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::007903333811:role/ROLE-PHC-LOGGING-01-UAT-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::576190738815:role/ROLE-GREDBUIT-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::053171596356:role/ROLE-PHC-QUARANTINE-01-UAT-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::851840725377:role/ROLE-PHC-PHICURATEDDATA-01-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::837830670462:role/ROLE-RSI-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::776542072855:role/ROLE-PHC-CURATED-DATA-01-UAT-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::250793067321:role/ROLE-GRED-CHEM-INFO-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::681276160618:role/ROLE-PHC-QUARANTINE-01-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::239183749126:role/ROLE-DISBUIT-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::741282338600:role/ROLE-PHC-VISUALIZATION-01-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::560927666947:role/ROLE-PHC-POC-SB-04-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::275747787338:role/ROLE-PHC-VISUALIZATION-01-UAT-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::641932311087:role/ROLE-GRED-SADR-01-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::427474886208:role/ROLE-PDIX-PHI-EDIS-DTT-CDSE-01-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::823666108077:role/ROLE-PDIX-PULSAR-01-DEV-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::110665395194:role/ROLE-GISIT-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::388008079775:role/ROLE-PHC-DEVSECOPS-01-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::675412887486:role/ROLE-PHC-LOGGING-01-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::107252309964:role/ROLE-PHC-PHIPRECURATED-01-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::486084566294:role/ROLE-APP-GIS-BUNVIDIA-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::277232114076:role/ROLE-PHC-DEVSECOPS-01-UAT-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::203520265514:role/ROLE-RSI-ECIS-001-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::466759258786:role/ROLE-SHARED-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::461923959893:role/ROLE-DMZ-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::588377792764:role/ROLE-GRED-GCORE-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::580410870115:role/ROLE-APP-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::345735039969:role/ROLE-PREDBUIT-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::958225524073:role/ROLE-GISIT-K8S-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::018820565695:role/ROLE-PHC-STAGING-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::619767159831:role/ROLE-PHC-ANALYTICS-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::890120545083:role/ROLE-PHC-DIGITAL-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::507987312224:role/ROLE-PHC-SHARED-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::411052296261:role/ROLE-PHC-DATA-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::047364797381:role/ROLE-pRED-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::857841613673:role/ROLE-gRED-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::042744687531:role/ROLE-PHC-POC-SB-01-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::102341992388:role/ROLE-PHC-POC-SB-02-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::428561211631:role/ROLE-PHC-POC-SB-03-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::868198829773:role/ROLE-PHC-RAAD-01-DEV-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::655759035838:role/ROLE-GRED-GERML-01-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::828338453436:role/ROLE-GRED-CNG-01-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::136707488073:role/ROLE-RMS-DAAP-01-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::059919589857:role/ROLE-PHC-HPC-01-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::139485587897:role/ROLE-PHC-BIOMETRIC-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::553314822239:role/ROLE-PHC-OMICS-SB-01-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::123102502338:role/ROLE-PHC-DATASCIENCE-TST-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::964196559594:role/ROLE-PTDC-ACDC-01-DEV-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::153041950703:role/ROLE-PRED-CLOUDP-APPSTACK-01-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::565385696047:role/ROLE-PRED-CLOUDP-ARVADOS-01-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::976188216412:role/ROLE-PRED-CLOUDP-TECHEVAL-01-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::219143015777:role/ROLE-PHC-NFERENCE-01-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::638921263575:role/ROLE-APP-GRED-BIPT-01-SB-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::153099027458:role/ROLE-RSI-ECIS-001-DEV-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::656460558808:role/ROLE-PRED-EDISON-01-DEV-LAMBDA-AD-ROUTE53-S3",
        "arn:aws:iam::070992492667:role/ROLE-PDIX-PULSAR-01-SB-SS-CROSSACCOUNT"
   ]

def vol_data(session,writer,account):
	regions = ["us-east-1","us-west-2","eu-central-1"]
	for region in regions:
		vol_details = {}
		client = session.client('ec2',region_name=region)


		vol_status = client.describe_volumes(Filters=[
        	{
            	'Name': 'status',
            	'Values': [
                	'available'
            	]
        	},
    	])

		for vol_id in vol_status['Volumes']:
			vol_details['Account_ID'] = account[4]
			vol_details['Region'] = region
			vol_details['VolumeId'] = vol_id['VolumeId']
			writer.writerow(vol_details)


def main():
	sts_client = boto3.client("sts")
	fieldnames = ["Account_ID","Region","VolumeId"]
	file_name = "vol_details.csv"
	with open (file_name,"w",newline='') as csv_file:
		writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
		writer.writeheader()
		for role_arn in roles:
		    sts_response = sts_client.assume_role(RoleArn = role_arn,RoleSessionName = "awstoaws")
		    session = boto3.Session(
		    aws_access_key_id = (sts_response["Credentials"]["AccessKeyId"]),
		    aws_secret_access_key = (sts_response["Credentials"]["SecretAccessKey"]),
		    aws_session_token = (sts_response["Credentials"]["SessionToken"]))
		    account = role_arn.split(":")
		    vol_data(session,writer,account)
main()

	
