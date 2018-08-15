# Connection to mysql DB
#from pymysql import *
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

    def save(self):
        self.name = str(input("Enter the Contact Name to be saved: "))
        self.mail = str(input("Enter the Email ID to the corresponding name: "))
        if self.name == "" or self.mail == "":
            print("Empty values are not accepted.")
            self.save()
            return False
        try:
            cur.execute('''INSERT INTO contacts VALUES("%s","%s")''',(self.name,self.mail))
            con.commit()
            print("Successfully saved")

            self.choice = str(input("Do you want to save another contancts? (Y/N)"))
            self.choice = self.choice.lower()

            if self.choice in ["y","yes"]:
                self.save()
            else:
                print("Exiting...")

        except pymysql.err.IntegrityError:
            print("Error : EmailId already exists")
            self.choice = str(input("Do you want to save another contancts? (Y/N)"))
            self.choice = self.choice.lower()

            if self.choice in ["y", "yes"]:
                self.save()
            else:
                return False

        return False

    def show(self):
        cur.execute('''SELECT * FROM contacts ''')
        for each in cur.fetchall():
            print("Name and corresponding Email ID:",each[0]," ",each[1])
        return False

    def fetch(self,name):
        cur.execute('''select emailid from contacts where name = %s''',(name))
        for x in cur.fetchall():
            self.name = x[0]
        return self.name






obj5 = Contact()
#obj5.save()
#obj5.show()
obj5.fetch("qwe")
