import commands
import smtplib
import datetime
today = datetime.date.today()

s = smtplib.SMTP('email-smtp.us-east-1.amazonaws.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("AKIAIISNA5O7X5J3ZFPA", "AopSM/RycfTZThdwIfvsnP8plE5WgpkTNJ00sUx9Z/3J")

#s = smtplib.SMTP('smtp.gmail.com', 587)
#s.starttls()
#s.login("ashwani.pal@hashedin.com", "rmripsrfyenqvagy")


# message to be sent
message ="""From:<alerts@hashedin.com>
To:<devops@hashedin.com>
Subject: Test Email
This is test Email please ignore This.

Regards,
DevOps"""

# sending the mail
s.sendmail("devops@hashedin.com","devops@hashedin.com", message)
#s.sendmail("devops@hashedin.com","devops@hashedin.com", message)
## attachments ##
#/tmp/EC2.csv /tmp/Project-based-ec2.csv /tmp/Project-based-rds.csv /tmp/RDS.csv
print "Email sent successfully......"
s.quit()
