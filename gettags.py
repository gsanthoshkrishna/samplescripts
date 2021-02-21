import boto3,sys,json
from dateutil.parser import parse
from datetime import datetime,timedelta

def update_ec2_tags():
	ec2 = boto3.client('ec2')
	resp = ec2.describe_instances()
	for reservation in resp['Reservations']:
	    for instance in reservation['Instances']:
	    	upd_tag = update_tags(instance['Tags'])
	    	#print(upd_tag)
	    	if upd_tag:
	    		ec2.create_tags(
	                Resources=[instance['InstanceId']],
	                Tags = [
	                    {
	                        'Key': 'Project',
	                        'Value': 'p1'
	                    }
	                ]
	            )



def rds_tags():
	print('Checking RDS Tags')
	rds = boto3.client('rds')
	db_inst_list = rds.describe_db_instances()
	for db_inst in db_inst_list['DBInstances']:
		print(db_inst)
		res_name = db_inst['TagList']
		print(res_name)
		upd_tag = update_tags(res_name)
		print(upd_tag)
		if upd_tag:
			rds.add_tags_to_resource(ResourceName=db_inst['DBInstanceArn'],Tags = [
	                    {
	                        'Key': 'Project',
	                        'Value': 'p1'
	                    }
	                ])

def update_tags(tags):
	foundccKey = False
	foundProjKey = False
	ccValue = "NA"
	acceptedCC = ['123','456','789']
	projValue = "NA"
	for tag in tags:
		print(tag)
		if tag['Key'] == 'cc':
			foundccKey = True
			if tag['Value'] in acceptedCC:
				ccValue = tag['Value']
		if tag['Key'] == 'Project':
			foundProjKey = True
			projValue = tag['Value']
	print(foundccKey)
	print(projValue != 'p1')
	print(ccValue)
	if foundccKey == False:
		print("Sending SNS Mail")
	if foundccKey == True and projValue != 'p1' and ccValue in acceptedCC:
		print("update tag")
		return True
	print("No UPdate")
	return False



#update_ec2_tags()
rds_tags()