#!/bin/bash

filename="921628772373-aws-billing-detailed-line-items-with-resources-and-tags-`date +%Y-%m`.csv"
loc='/home/hashedin/AWS_SECURITY_AUDIT/daily_bill'
old_file='hiawsca_orig.csv'
new_file='hiawsca.csv'
s3_loc='s3://hi-aws-billing'
script_loc='/home/hashedin/AWS_SECURITY_AUDIT'

cd $loc
#rm -f `date +%d%m%y`.csv
s3cmd get $s3_loc/$filename.zip
unzip $filename.zip
mv $filename $old_file
rm -f *.zip
python $script_loc/script.py
rm $old_file
