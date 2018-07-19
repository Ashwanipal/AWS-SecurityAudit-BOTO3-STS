#/bin/bash
mysqldump -u root -ppass123 hiawsca > /home/hashedin/DB_Backup/HI-awsca-`date +%d%m%y`.sql
