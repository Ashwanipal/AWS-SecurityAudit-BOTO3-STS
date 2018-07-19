import commands
import os

#os.system("echo '<html><h2>AWS alert! You have ports open for all on security-groups</h2>'>/tmp/sg_data.html")

#Configure the AWS cross account role and add the ARN here
arns1=["arn:01", "arn:02", "arn:03"]

f1=open('/tmp/email_output.html', 'a')
f1.write("<div style='width:90%;'><hr><h1>Cost Summary</h1>")
f1.write("<table style='width:98%', border='1'><thead><th>Account Name</th><th>Account ID</th><th>Cost Breakdown</th></thead><tbody>")
f1.close()
for arn in arns1:
        a=commands.getoutput("sudo python /home/some_DIR/AWS_SECURITY_AUDIT/sg_scripts/cost_estimate.py  "+arn)
        print arn

total_cost=commands.getoutput("mysql -u root -ppass123 HI_BILLING -e 'select SUM(ca_Cost) as Cost from hiaws_ca;' | sed -n '1!p'")
f1=open('/tmp/email_output.html', 'a')
f1.write("<tr><td>-</td><td><b>Consolidated Total Bill</b></td><td><b>"+total_cost+" $</b></td></tr>")
f1.write("</tbody></table></br><h1>Security Summary</h1><hr>")
f1.close()

arns=["arn:01", "arn:02", "arn:03"]
        a=commands.getoutput("sudo python /home/some_DIR/AWS_SECURITY_AUDIT/sg_scripts/sg_open_port.py  "+arn)
        print arn

