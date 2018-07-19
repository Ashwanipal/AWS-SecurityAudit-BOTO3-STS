import commands
import smtplib
import datetime
today = datetime.date.today()

s = smtplib.SMTP('email-smtp.us-east-1.amazonaws.com', 587)

# start TLS for security

s.starttls()

# Authentication (Provied SES cradentials here)

s.login("key", "pass")

f = open("/tmp/email_output.html","r")
a=(f.read())
#print a
f.close()

# message to be sent
message ="""From:<alerts@example.com>
To:<alerts@example.com>
Content-type: text/html
Subject:"""+str(today)+""" AWS Security / Cost Audit
%s"""%(a)

# sending the mail
s.sendmail("alerts@example.com","alerts@example.com", message)
## attachments ##
print "["+str(datetime.datetime.now())+"] Email sent successfully......"
s.quit()
