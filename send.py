import commands
import smtplib
import datetime
today = datetime.date.today()

s = smtplib.SMTP('email-smtp.us-east-1.amazonaws.com', 587)

# start TLS for security

s.starttls()

# Authentication

s.login("AKIAIISNA5O7X5J3ZFPA", "AopSM/RycfTZThdwIfvsnP8plE5WgpkTNJ00sUx9Z/3J")

f = open("/tmp/email_output.html","r")
a=(f.read())
#print a
f.close()

# message to be sent
message ="""From:<alerts@hashedin.com>
To:<devops@hashedin.com>
Content-type: text/html
Subject:"""+str(today)+""" HashedIn AWS Security / Cost Audit
%s"""%(a)

# sending the mail
#s.sendmail("ashwani.pal@hashedin.com","ashwani.pal@hashedin.com", message)
s.sendmail("devops@hashedin.com","devops@hashedin.com", message)
## attachments ##
#/tmp/EC2.csv /tmp/Project-based-ec2.csv /tmp/Project-based-rds.csv /tmp/RDS.csv
print "["+str(datetime.datetime.now())+"] Email sent successfully......"
s.quit()
