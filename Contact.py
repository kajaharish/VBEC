# Connection to mysql DB
#from pymysql import *
import pymysql
con = pymysql.connect("localhost","root","","test" )
cur=con.cursor()

# Creation of table Employer
class Contact:

    # sql=("""CREATE TABLE Employer(
    #         CompanyID varchar(5) NOT NULL PRIMARY KEY,
    #     CompanyName Varchar(50) NOT NULL,
    #     EmailID Varchar(30),
    #     Mobile Bigint(10) CHECK (length(Mobile) = 10),
    #     City Varchar(15),
    #     IndustryType Varchar(20),
    #     FunctionalArea Varchar(20),
    #     MembershipPlan Varchar(20) CHECK (MembershipPlan IN('Trial','Monthly','Yearly')),
    #     DateofSignup TIMESTAMP DEFAULT CURRENT_TIMESTAMP CHECK (DateofSignup >= CURRENT_TIMESTAMP),
    #     DateofRenewal TIMESTAMP,
    #     RenewalStatus varchar(10) CHECK (RenewalStatus IN ('Active','Expired'))
    #     )
    #     """)
    # cur.execute(sql)

    def save(self):
        self.name = str(input("Enter the Contact Name to be saved: "))
        self.mail = str(input("Enter the Email ID to the corresponding name: "))
        cur.execute('''INSERT INTO contacts VALUES("%s","%s")''',(self.name,self.mail))
        con.commit()
        self.choice = str(input("Do you want to save more contancts? (Y/N)"))
        self.choice = self.choice.lower()

        if self.choice in ["y","yes"]:
            self.save()
        else:
            return
        return



    # con.commit()
    #
    #
    #
    #
    # #close Connection
    # con.close()
obj5 = Contact()
obj5.save()
