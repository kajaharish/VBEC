# Connection to mysql DB
#from pymysql import *
import re

import pymysql

con = pymysql.connect("localhost","root","","test" )
cur=con.cursor()

# Creation of table Employer
class Contact:

    # sql=("""CREATE TABLE contacts(
    #     Name varchar(45) NOT NULL,
    #     EmailId varchar(45) NOT NULL PRIMARY KEY)
    #     """)
    # cur.execute(sql)

    def isValidEmail(self,email):
        if len(email) > 7:
            if re.match("^.+@([?)[a-zA-Z0-9-.])+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) is not None:
                return True
        return False


    def save(self):
        self.name = str(input("Enter the Contact Name to be saved: "))
        self.mail = str(input("Enter the Email ID to the corresponding name: "))

        if self.isValidEmail(self.mail) == True:
            if self.name == "" or self.mail == "":
                print("Empty values are not accepted.")
                self.save()
                return False
            try:
                cur.execute("""INSERT INTO contacts VALUES(%s,%s)""",(self.name,self.mail))
                con.commit()
                print("Successfully saved")

                self.choice = str(input("Do you want to save another contancts? (Y/N)"))
                self.choice = self.choice.lower()

                if self.choice in ["y","yes"]:
                    self.save()
                else:
                    print("Exiting...")

            except pymysql.err.IntegrityError:
                print("\nError : EmailId already exists")
                self.choice = str(input("Do you want to save another contancts? (Y/N)"))
                self.choice = self.choice.lower()

                if self.choice in ["y", "yes"]:
                    self.save()
                else:
                    return False
        else:
            print("\n\nEntered E-mail ID is invalid.\n")
            self.save()

            return False

    def show(self):
        cur.execute('''SELECT * FROM contacts ''')
        for each in cur.fetchall():
            print("Name and corresponding Email ID:",each[0]," ",each[1])
        return False


    def fetch(self,name):
        try:
            cur.execute('''select emailid from contacts where name = %s''',(name))
            for x in cur.fetchall():
                self.name = x[0]
            return self.name
        except:
            print("Contact doesn't Exist.")
            con.close()


    def delete(self,name):
        try:
            cur.execute('''delete from contacts where name = %s''',(name))
            print("Successfully Deleted.")
            con.commit()
            return True
        except:
            print("Please enter the correct contact details.")
            con.close()
            return False






# obj5 = Contact()
# obj5.save()
# obj5.show()
# obj5.fetch('drag')
# obj5.delete("qwe")

