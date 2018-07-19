#!/bin/bash

filename="S3-billing-CSV-name.csv"
loc='/home/some_DIR/AWS_SECURITY_AUDIT/daily_bill'
old_file='old.csv'
new_file='new.csv'
s3_loc='s3://your-bucket-name/'
script_loc='/home/som-DIR/AWS_SECURITY_AUDIT'

cd $loc
#rm -f `date +%d%m%y`.csv
s3cmd get $s3_loc/$filename.zip
unzip $filename.zip
mv $filename $old_file
rm -f *.zip
python $script_loc/script.py
rm $old_file
