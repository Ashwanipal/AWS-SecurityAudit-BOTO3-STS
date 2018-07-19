#/bin/bash
mysqldump -u root -ppass123 DB_name > /home/some_DIR/DB_Backup/HI-awsca-`date +%d%m%y`.sql
