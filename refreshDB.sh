#!/bin/sh

######### Cradentials ################################
MUSQL_USER="root"
MYSQL_PASS="pass123"
MYSQL_DB="DB_NAME"

########## Refreshing Database #######################
mysql -u $MUSQL_USER -p$MYSQL_PASS $MYSQL_DB -e 'truncate table_name;'
mysql -u $MUSQL_USER -p$MYSQL_PASS $MYSQL_DB --local-infile < /home/some_DIR/AWS_SECURITY_AUDIT/load-data

######### cost estimation ##########
#total=$(mysql -u $MUSQL_USER -p$MYSQL_PASS $MYSQL_DB -e "select SUM(ca_Cost) as Cost from hiaws_ca where ca_LinkedAccountId = "$ID";" | sed -n '1!p')
#total_cost=$(mysql -u $MUSQL_USER -p$MYSQL_PASS $MYSQL_DB -e 'select SUM(ca_Cost) as Cost from table_name;' | sed -n '1!p')

