select ifnull(ca_UserApp,'Grand Total'), SUM(ca_Cost) as Cost from hiaws_ca where ca_ProductName='Amazon Elastic Compute Cloud' group by ca_UserApp with rollup INTO OUTFILE '/tmp/Project-based-ec2.csv' FIELDS TERMINATED BY ','  ENCLOSED BY '"' LINES TERMINATED BY '\n';

select ifnull(ca_UserApp,'Grand Total'), SUM(ca_Cost) as Cost from hiaws_ca where ca_ProductName='Amazon RDS Service' group by ca_UserApp with rollup INTO OUTFILE '/tmp/Project-based-rds.csv' FIELDS TERMINATED BY ','  ENCLOSED BY '"' LINES TERMINATED BY '\n';


select ifnull(ca_UserName,'Grand Total'),ca_ProductName as Service,SUM(ca_Cost) as Cost,SUBSTRING(MIN(ca_UsageStartDate),1,10) as StartDate,SUBSTRING(MAX(ca_UsageEndDate),1,10) as EndDate from hiaws_ca where ca_ProductName='Amazon Elastic Compute Cloud' group by ca_UserName with rollup INTO OUTFILE '/tmp/EC2.csv' FIELDS TERMINATED BY ','  ENCLOSED BY '"' LINES TERMINATED BY '\n';

select ifnull(SUBSTRING(ca_ResourceId,39,15),'Grand Total') as ProjectName,ca_ProductName as Service,SUM(ca_Cost) as Cost,SUBSTRING(MIN(ca_UsageStartDate),1,10) as StartDate,SUBSTRING(MAX(ca_UsageEndDate),1,10) as EndDate from hiaws_ca where ca_ProductName='Amazon RDS Service' group by ca_ResourceId with rollup INTO OUTFILE '/tmp/RDS.csv'  FIELDS TERMINATED BY ','  ENCLOSED BY '"' LINES TERMINATED BY '\n';
