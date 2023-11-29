import pymongo
import random
client = pymongo.MongoClient('mongodb+srv://naveenchandgadde:ChanduG97@flask.0zcjxbr.mongodb.net/')
mydb = client['Employee']
information=mydb.table2
employeeno = []
n=int(input("Enter number of Employees : "))
for i in range(n):
    Emp_no = random.randint(1,4)
    Emp_Name=input("Enter Employee Name : ")
    Emp_Org=input("Enter Organization Name : ")
    Job_Role=input("Enter Role of Employee : ")
    Hire_Date=input("Enter Joining Date : ")
    dept_no=int(input("Enter Dept No : "))
    Sal=float(input("Enter your Salary : "))
    records=[{
        "Emp NO" : Emp_no,
        "Emp Name" : Emp_Name,
        "Emp_Org" : Emp_Org,
        "Job":Job_Role,
        "Hire Date":Hire_Date,
        "Dept NO":dept_no,
        "Salary" : Sal
    }]
    information.insert_many(records)

class Employees:
    def __init__(self, name):
        self.name = name
        self.relationships = []

class Organization:
    def __init__(self, name):
        self.name = name
Employees.name=Emp_Name
Organization.name=Emp_Org
print(Employees.name)
print(Organization.name)
print('-'*50,"\nEntered Details are pushed to MongoDB successfully")