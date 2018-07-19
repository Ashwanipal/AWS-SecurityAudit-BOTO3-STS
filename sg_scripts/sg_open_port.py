import json
import boto
import boto3
import os
import commands
import boto.ec2
from boto import ec2
from boto.sts import STSConnection
import sys

arn=str(sys.argv[1])
print  arn
sts_connection = STSConnection()
assumed_role_object = sts_connection.assume_role(
role_arn=arn,
role_session_name="run-script"
)
os.environ["AWS_ACCESS_KEY_ID"] =assumed_role_object.credentials.access_key
os.environ["AWS_SECRET_ACCESS_KEY"] = assumed_role_object.credentials.secret_key
os.environ["AWS_SESSION_TOKEN"] = assumed_role_object.credentials.session_token

############ Get Account name & ID #############################################
accountname=commands.getoutput("aws iam list-account-aliases | awk {'print $2'}")
accountid=(boto3.client('sts').get_caller_identity()['Account'])
print accountname
f1=open('/tmp/email_output.html', 'a')
f1.write("<h2 style='color:#0066cc;'>"+accountname+" ["+accountid+"]</h2><hr>\n<h4>Security Group Ports Summary for EC2 Instances</h4>\n<table style=\'width:100%\', border=\'1\'>\n<thead><th>Instance Name</th><th>Instance Type</th><th>VPC</th><th>Security Group</th><th>Ports Opened</th></thead>\n<tbody>\n")

############# EC2 instance INFo with attached security group name/ID ###########
def get_name(instance):
	if instance.tags:
        	for tag in instance.tags:
        	        if tag['Key'] == 'Name':
                	        return tag['Value']


ec2 = boto3.resource('ec2')
instances = ec2.instances.filter()
for instance in instances:
        vpc_id=str(instance.vpc_id)
        sginfo=""
        security=""
        for sg in instance.security_groups:
                for sg in boto3.client('ec2', region_name="us-east-1").describe_security_groups(GroupIds=[sg['GroupId']])['SecurityGroups']:
                        toport=[]
                        frport=[]
                        sgi= sg['GroupId']
                        sgn= sg['GroupName']
                        ippermission=sg['IpPermissions']
                        for ip in ippermission:
                                cidrs=ip['IpRanges']
                                for cidr in cidrs:
                                        try:
                                                cidr= cidr['CidrIp']
                                                tport=ip['ToPort']
                                                fport=ip['FromPort']
                                                if cidr=='0.0.0.0/0' and str(ip['ToPort']) != "80" and str(ip['ToPort']) != "443":
                                                        security +="<span style='color:red;'>"+cidr+" | To-port:"+str(tport)+" | From-port:"+str(fport)+"</span><br>"
                                                else:
                                                        security += cidr+" | To-port:"+str(tport)+" | From-port:"+str(fport)+"<br>"
                                        except:
                                                        print "Error"
                        sginfo += sgi+"<br>"

        flag="<tr><td>" +str(get_name(instance))+ "</td><td>"+instance.instance_type+"</td><td>" + vpc_id +"</td><td>"+sginfo+"</td><td>"+ security+"</td></tr>\n"
        f1.write(flag)

	#print flag
f1.write("</tbody></table><h4>Security Group Ports Summary for RDS Instances</h4>\n<table style=\'width:100%\', border=\'1\'>\n<thead><th>Instance Name</th><th>VPC</th><th>Security Group and Ports Opened</th></thead>\n<tbody>\n")

############## get all RDS instance name with group name ###############

for rds in boto3.client('rds', region_name='us-east-1').describe_db_instances()['DBInstances']:
        instance = rds['MasterUsername']
        Rsginfo=""
        for vpcsg in rds['VpcSecurityGroups']:
                sg_name = vpcsg['VpcSecurityGroupId']
                for sg in boto3.client('ec2', region_name="us-east-1").describe_security_groups(GroupIds=[sg_name])['SecurityGroups']:
                        toport=[]
                        frport=[]
                        sgi= sg['GroupId']
                        #sgn= sg['GroupName']
                        ippermission=sg['IpPermissions']
                        for ip in ippermission:
                                cidrs=ip['IpRanges']
                                for cidr in cidrs:
                                        cidr= cidr['CidrIp']
                                        #print cidr
                                        if 'ToPort' in ip and cidr=='0.0.0.0/0' and str(ip['ToPort']) != "80" and str(ip['ToPort']) != "443":
                                                try:
                                                        toport.append(ip['ToPort'])
                                                        frport.append(ip['FromPort'])
                                                except:
                                                        print "Error"
                        if toport != []:
                                port= str(toport)
                                Rsginfo +="GROUP-ID : "+sgi+" | PORTS : <span style='color:red;'>"+port+"</span><br>"
	if Rsginfo != "":
        	flag1= "<tr><td>"+instance+"</td><td>-</td><td>"+Rsginfo+"</td></tr>\n"
        	f1.write(flag1)
        	#print flag1
f1.write("</tbody></table><h4>Publically Accessible Security Group Ports</h4>\n<table style=\'width:100%\', border=\'1\'>\n<thead><th>Security Group</th><th>ID</th><th>Ports Opened</th></thead>\n<tbody>\n")

for sg in boto3.client('ec2', region_name="us-east-1").describe_security_groups()['SecurityGroups']:
	cidr=""
        toport=[]
        frport=[]
        sgi=sg['GroupId']
        sgn=sg['GroupName']
        ippermission=sg['IpPermissions']
	print "---------------------------------------------------------------------------------------"
        for ip in ippermission:
        	cidrs=ip['IpRanges']
                for cidr in cidrs:
                	cidr = cidr['CidrIp']
			try:
                        	if cidr=='0.0.0.0/0' and str(ip['ToPort']) != "80" and str(ip['ToPort']) != "443":
                        		toport.append(ip['ToPort'])
                                        frport.append(ip['FromPort'])
                        except:
                           	print "Error"
	if toport != []:
        	toport = str(toport)
		frport = str(frport)
        	flag3="<tr><td>"+sgn+"</td><td>"+sgi+"</td><td style='color:red;'>"+toport+"</td></tr>\n"
		f1.write(flag3)

f1.write("</tbody></table>")
f1.write("<h4>IAM Users Summary</h4><table style=\'width:100%\', border=\'1\'>\n<thead><th>Username</th><th>MFA Status</th><th>User Created</th><th>Last Login</th></thead>\n<tbody>\n")


client = boto3.client('iam')
iam = boto3.client("iam")
users = client.list_users()
for key in users['Users']:
	uname=key['UserName']
	createD=key['CreateDate'].date()
	if 'PasswordLastUsed' in key:
      		lastlogin=key['PasswordLastUsed'].date()
    	else:
      		lastlogin="null"
	mfa = iam.list_mfa_devices(UserName=key['UserName'])
        if len(mfa["MFADevices"]) > 0:
                MFA="<span style='color:#558000;'>Active</span>"
        else:
                MFA="<span style='color:#ff0000;'>In-Active</span>"

    	flag4="<tr><td>"+str(uname)+"</td><td>"+str(MFA)+"</td><td>"+str(createD)+"</td><td>"+str(lastlogin)+"</td></tr>"
	f1.write(flag4)
	MFA=""
f1.write("</tbody></table>")

###################### new launched EC2 instances ############################
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
        if creator != "" and str(instance["LaunchTime"].date()) == str(datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')):
                flage5="<tr><td>"+instance["InstanceId"]+"</td><td>"+instance["InstanceType"]+"</td><td>"+str(instance["LaunchTime"].date())+"</td><td>"+requestor+"</td><td>"+creator+"</td></tr>"
                print flage5
        instancedetails = instancedetails + flage5
        flage5 =""
if instancedetails != "":
        f1=open('/tmp/email_output.html', 'a')
        f1.write("<h3>EC2 Instances Launched Yesterday</h3><table style='width:98%', border='1'><thead><th>Instance-ID</th><th>Type</th><th>Launch Date</th><th>Requestor</th><th>Creator</th></thead><tbody>")
        f1.write(instancedetails)
	f1.write("</tbody></table>")
        f1.close()


f1.close()

