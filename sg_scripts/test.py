import json
import boto
import boto3
import os
import commands
import boto.ec2
from boto import ec2
from boto.sts import STSConnection

arn= "arn:aws:iam::921628772373:role/test"
#arn="arn:aws:iam::421314253251:role/HI-Security"
sts_connection = STSConnection()
assumed_role_object = sts_connection.assume_role(
role_arn=arn,
role_session_name="anka"
)
os.environ["AWS_ACCESS_KEY_ID"] =assumed_role_object.credentials.access_key
os.environ["AWS_SECRET_ACCESS_KEY"] = assumed_role_object.credentials.secret_key
os.environ["AWS_SESSION_TOKEN"] = assumed_role_object.credentials.session_token

print(boto3.client('sts').get_caller_identity()['Account'])
instancedetails=""
flage5=""
requestor=""
creator=""
from datetime import datetime, timedelta
ec2client = boto3.client('ec2')
response = ec2client.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
	for tag in instance["Tags"]:
		try:
			if tag["Key"] == "requestor":
				requestor=tag["Value"]
			if tag["Key"] == "creator":
				creator=tag["Value"]
		except:
			print "Error"
        if creator != "" and str(instance["LaunchTime"].date()) == str(datetime.strftime(datetime.now(), '%Y-%m-%d')):
		flage5="<tr><td>"+instance["InstanceId"]+"</td><td>"+instance["InstanceType"]+"</td><td>"+str(instance["LaunchTime"].date())+"</td><td>"+requestor+"</td><td>"+creator+"</td></tr></tbody></table>"
		print flage5
	instancedetails = instancedetails + flage5
	flage5 =""
if instancedetails != "":
	f1=open('/tmp/email_output.html', 'a')
	f1.write("<h3>New launched EC2 instances</h3><table style='width:98%', border='1'><thead><th>Instance-ID</th><th>Type</th><th>Launch Date</th><th>Requestor</th><th>Creator</th></thead><tbody>")
	f1.write(instancedetails)
	f1.close()

from datetime import datetime, timedelta
print datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
print datetime.strftime(datetime.now(), '%Y-%m-%d')

