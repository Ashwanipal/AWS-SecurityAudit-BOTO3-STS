'''
    @author: Pawan Tejwani
    @contact: pawan.tejwani@hashedin.com / +919766003668
'''

FILENAME = "/home/hashedin/AWS_SECURITY_AUDIT/daily_bill/hiawsca_orig.csv"
OUTFILE = "/home/hashedin/AWS_SECURITY_AUDIT/daily_bill/hiawsca.csv"


import csv
######### Create Table in database ##########
##CREATE TABLE hiaws_ca (ca_PayerAccountId varchar(70), ca_LinkedAccountId varchar(30), ca_ProductName varchar(70), ca_UsageType varchar(30), ca_AvailabilityZone varchar(15), ca_ItemDescription varchar(99), ca_UsageStartDate TIMESTAMP DEFAULT 0, ca_UsageEndDate TIMESTAMP DEFAULT 0, ca_UsageQuantity decimal(8,8), ca_Cost decimal(2,2), ca_ResourceId varchar(50), ca_UserName varchar(25), ca_UserApp varchar(10), ca_UserEnv varchar(5));
## initialize variables to be put in database (following is database structure)
# | Column Name         | Data Type    |      |     | Default Value       |       |
# | ca_PayerAccountId   | varchar(70)  | YES  |     | NULL                |       |
# | ca_LinkedAccountId  | varchar(30)  | YES  |     | NULL                |       |
# | ca_ProductName      | varchar(70)  | YES  |     | NULL                |       |
# | ca_UsageType        | varchar(30)  | YES  |     | NULL                |       |
# | ca_AvailabilityZone | varchar(15)  | YES  |     | NULL                |       |
# | ca_ItemDescription  | varchar(99)  | YES  |     | NULL                |       |
# | ca_UsageStartDate   | timestamp    | NO   |     | 0000-00-00 00:00:00 |       |
# | ca_UsageEndDate     | timestamp    | NO   |     | 0000-00-00 00:00:00 |       |
# | ca_UsageQuantity    | decimal(8,8) | YES  |     | NULL                |       |
# | ca_Cost             | decimal(2,2) | YES  |     | NULL                |       |
# | ca_ResourceId       | varchar(50)  | YES  |     | NULL                |       |
# | ca_UserName         | varchar(25)  | YES  |     | NULL                |       |
# | ca_UserApp          | varchar(10)  | YES  |     | NULL                |       |
# | ca_UserCreator      | varchar(20)  | YES  |     | NULL                |       |
# | ca_UserEnv          | varchar(5)   | YES  |     | NULL                |       |
# | ca_UserOwner        | varchar(20)  | YES  |     | NULL                |       |
# | ca_UserRequestor    | varchar(20)  | YES  |     | NULL                |       |
# | ca_UserName		| varchar(25)  | YES  |	    | NULL		  |       |
# | ca_UserApp		| varchar(10)  | YES  |	    | NULL		  |       |
# | ca_UserEnv		| varchar(5)  | YES  |	    | NULL		  |       |

def date_converter(datevar):
    if ((str)(datevar)).__eq__(""):
        return "0000-00-00 00:00:00"
    tmp = ((str)(datevar)).split(" ")
    ## tmp[0] will have date
    ## tmp[1] will have time
    tmp[0] = ((str)(tmp[0])).split("-")
    tmp[1] = ((str)(tmp[1])).split(":")
    tmp1 = (str)(tmp[0][0])+"-"+(str)(tmp[0][1])+"-"+(str)(tmp[0][2])+" "+(str)(tmp[1][0])+":"+(str)(tmp[1][1])+":00"
    return tmp1


#  f6 f10 f12 f14 f15 f16 f17 f19 f20 f21 f22 f23 f24 f25 f26 f27
## Data in csv file is read from "Column 0"
ca_PayerAccountId = ""	
ca_LinkedAccountId = ""
ca_ProductName = ""             ## Col 5
ca_UsageType = ""               ## Col 9
ca_AvailabilityZone = ""        ## Col 11
ca_ItemDescription = ""         ## Col 13
ca_UsageStartDate = ""          ## Col 14
ca_UsageEndDate = ""            ## Col 15
ca_UsageQuantity = ""           ## Col 16
ca_Cost = ""                    ## Col 18
ca_ResourceId = ""              ## Col 21
ca_UserName = ""                ## Col 26
ca_UserApp = ""                 ## Col 27
ca_UserEnv = ""                 ## Col 30
error = 0


## check if formatted csv file already exists
f=open(OUTFILE,'w')
with open(FILENAME,'rb') as csvfile:
    content = csv.reader(csvfile, delimiter=',', quotechar = '"')
    for row in content:
        try:
            if (((str)(row[3])).__contains__("LineItem")):
                ## Assign only if it's a line item
		ca_PayerAccountId = ((str)(row[1]))
		ca_LinkedAccountId = ((str)(row[2]))
                ca_ProductName = ((str)(row[5]))
                ca_UsageType = ((str)(row[9]))
                ca_AvailabilityZone = ((str)(row[11]))
                ca_ItemDescription = '"'+((str)(row[13]))+'"'
                ca_UsageStartDate = ((str)(date_converter((str)(row[14]))))
                ca_UsageEndDate = ((str)(date_converter((str)(row[15]))))
                ca_UsageQuantity = ((str)(row[16]))
                ca_Cost = ((str)(row[18]))
                ca_ResourceId = ((str)(row[21]))
                ca_UserName = ((str)(row[23]))
                ca_UserApp = ((str)(row[25]))
                ca_UserEnv = ((str)(row[25])) #Need to be change
                f.write((str)(ca_PayerAccountId+","+ca_LinkedAccountId+","+ca_ProductName+","+ca_UsageType+","+ca_AvailabilityZone+","+ca_ItemDescription+","+ca_UsageStartDate+","+ca_UsageEndDate+","+ca_UsageQuantity+","+ca_Cost+","+ca_ResourceId+","+ca_UserName+","+ca_UserApp+","+ca_UserEnv+"\n"))
        except:
            ## we will then log the error in log file
            error = 0
f.close()

print OUTFILE + " updated"
