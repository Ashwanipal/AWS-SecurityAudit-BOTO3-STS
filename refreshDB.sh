#!/bin/sh

######### Cradentials ################################
MUSQL_USER="root"
MYSQL_PASS="pass123"
MYSQL_DB="DB_NAME"

########## Refreshing Database #######################
mysql -u $MUSQL_USER -p$MYSQL_PASS $MYSQL_DB -e 'truncate table_name;'
mysql -u $MUSQL_USER -p$MYSQL_PASS $MYSQL_DB --local-infile < /home/some_DIR/AWS_SECURITY_AUDIT/load-data
