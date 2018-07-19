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

MYSQL_USER="root"
MYSQL_PASS="pass123"
MYSQL_DB="HI_BILLING"

############ Get Account name & ID #############################################
accountname=commands.getoutput("aws iam list-account-aliases | awk {'print $2'}")
accountid=(boto3.client('sts').get_caller_identity()['Account'])

total=commands.getoutput("mysql -u "+MYSQL_USER+" -p"+MYSQL_PASS+" "+MYSQL_DB+" -e 'select SUM(ca_Cost) as Cost from hiaws_ca where ca_LinkedAccountId = "+accountid+";' | sed -n 1!p")

f1=open('/tmp/email_output.html', 'a')
f1.write("<tr><td><b>"+accountname+"</b></td><td>"+accountid+"</td><td>"+total+"</td></tr>")
f1.close()

