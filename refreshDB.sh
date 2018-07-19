#!/bin/sh

######### Cradentials ################################
MUSQL_USER="root"
#MYSQL_PASS="ankur"
MYSQL_PASS="pass123"
MYSQL_DB="HI_BILLING"

########## Refreshing Database #######################
mysql -u $MUSQL_USER -p$MYSQL_PASS $MYSQL_DB -e 'truncate hiaws_ca;'
mysql -u $MUSQL_USER -p$MYSQL_PASS $MYSQL_DB --local-infile < /home/hashedin/AWS_SECURITY_AUDIT/load-data

######### cost estimation ##########
#total=$(mysql -u $MUSQL_USER -p$MYSQL_PASS $MYSQL_DB -e "select SUM(ca_Cost) as Cost from hiaws_ca where ca_LinkedAccountId = "$ID";" | sed -n '1!p')
#total_cost=$(mysql -u $MUSQL_USER -p$MYSQL_PASS $MYSQL_DB -e 'select SUM(ca_Cost) as Cost from hiaws_ca;' | sed -n '1!p')

