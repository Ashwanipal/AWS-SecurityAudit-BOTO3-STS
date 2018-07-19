import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from email import Encoders
fromaddr = "ashwani.pal@hashedin.com"
toaddr = "ashwani.pal@hashedin.com"
print "Sending Email.....";
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "AWS COST & SECURITY AUDIT"

f = open("/tmp/email_output.html","r")
a=(f.read())
f.close()
############# Message to be send #################
body = "%s"%(a)
msg.attach(MIMEText(body, 'html'))

############# Attachments ########################
attachments = ['EC2.csv', 'Project-based-ec2.csv', 'Project-based-rds.csv', 'RDS.csv']
if 'attachments' in globals() and len('attachments') > 0: # are there attachments?
        for filename in attachments:
            f = filename
            part = MIMEBase('application', "octet-stream")
            part.set_payload( open('/tmp/'+f,"rb").read() )
            Encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % filename)
            msg.attach(part)

########### Email authantantication & send Email ##
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("ashwani.pal@hashedin.com", "rmripsrfyenqvagy")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
print "Sucsessfully sended ...........";
server.quit()
