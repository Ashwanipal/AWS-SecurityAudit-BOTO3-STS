#!/bin/sh

######### Cradentials ################################
MUSQL_USER="root"
MYSQL_PASS="ankur"
MYSQL_DB="HI_BILLING"

#select date_format(ca_UsageEndDate,'%Y-%m-%d') from hiaws_ca group by date_format(ca_UsageEndDate,'%Y-%m-%d')
#AC_IDs=$(mysql -u $MUSQL_USER -p$MYSQL_PASS $MYSQL_DB -e "SELECT ca_LinkedAccountId FROM hiaws_ca GROUP BY ca_LinkedAccountId;" | sed -n '1!p')
#echo $AC_IDs
#for AC_ID in $AC_IDs
#do
	#mysql -u $MUSQL_USER -p$MYSQL_PASS $MYSQL_DB -e "select date_format(ca_UsageEndDate,'%Y-%m-%d'), SUM(ca_Cost) as Cost from hiaws_ca where ca_LinkedAccountId = "$AC_ID";"
#	echo "$AC_ID"
#	i
	#dates=$(mysql -u $MUSQL_USER -p$MYSQL_PASS $MYSQL_DB -e "select date_format(ca_UsageEndDate,'%Y-%m-%d') from hiaws_ca where LinkedAccountId = "$AC_ID";")
	#	for dat in dates
	#	do
			
	
#done
ACID=$(mysql -u $MUSQL_USER -p$MYSQL_PASS $MYSQL_DB -e "SELECT ca_LinkedAccountId FROM hiaws_ca GROUP BY ca_LinkedAccountId;" | sed -n '1!p')
for ID in $ACID
do
	dates=$(mysql -u $MUSQL_USER -p$MYSQL_PASS $MYSQL_DB -e "select date_format(ca_UsageEndDate,'%Y-%m-%d') from hiaws_ca group by date_format(ca_UsageEndDate,'%Y-%m-%d')" | sed -n '1!p')
	echo "Account ID : $ID"
	for date in $dates
	do
		Cost=$(mysql -u $MUSQL_USER -p$MYSQL_PASS $MYSQL_DB -e "select SUM(ca_Cost) from hiaws_ca where ca_LinkedAccountId = "$ID" AND date_format(ca_UsageEndDate,'%Y-%m-%d') = '"$date"';" | sed -n '1!p')
		echo "DATE : $date  COST : $Cost"
	done
done

#dates=$(mysql -u $MUSQL_USER -p$MYSQL_PASS $MYSQL_DB -e "select date_format(ca_UsageEndDate,'%Y-%m-%d') from hiaws_ca group by date_format(ca_UsageEndDate,'%Y-%m-%d')" | sed -n '1!p')
#for date in $dates
#do
#	echo $date
#done
