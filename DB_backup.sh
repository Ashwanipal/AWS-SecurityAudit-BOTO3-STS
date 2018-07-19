#/bin/bash
mysqldump -u root -ppass123 hiawsca > /home/some_DIR/DB_Backup/HI-awsca-`date +%d%m%y`.sql
