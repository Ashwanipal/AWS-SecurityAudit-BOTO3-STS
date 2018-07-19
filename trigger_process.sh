#!/bin/bash
echo "<html><body><p>This is an automated notification email for HashedIn AWS consolidated daily audit report for Cost and Security.</p>" >/tmp/email_output.html
script_loc='/home/hashedin/AWS_SECURITY_AUDIT'

###### Downloding the CSV file from S3 #######
bash $script_loc/get_csv.sh

##### refreshing Database ####################
bash $script_loc/refreshDB.sh
echo "Database refreshed......"
##### Security group & cost estimation########
python $script_loc/sg_scripts/run.py
echo "<br>Regards,<br>DevOps</body></html>" >>/tmp/email_output.html

##### Send email with Attachment #############
#python $script_loc/send.py
