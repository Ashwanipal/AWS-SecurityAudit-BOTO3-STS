
Disable Modes in MYSQL
	Open the file /etc/mysql/my.cnf and add the following [Ignore modes => NO_ZERO_IN_DATE, NO_ZERO_DATE, ONLY_FULL_GROUP_BY]
	>> [mysqld]
	>> sql_mode = "STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"

Disable secure-file-priv to store MYSQL query output in file

	For Ubuntu, edit the file /etc/mysql/mysql.conf.d/mysqld.cnf and add the following line at the end:
	>> secure_file_priv=""
	Then make sure to restart the service.
