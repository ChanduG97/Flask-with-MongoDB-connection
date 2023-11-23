import pymongo
from flask import Flask, jsonify
client = pymongo.MongoClient('mongodb+srv://naveenchandgadde:ChanduG97@flask.0zcjxbr.mongodb.net/')
mydb = client['Employee']
information=mydb.table1

n=int(input("Enter number of Employees : "))
for i in range(n):
    Emp_no=int(input("Enter Employee No : "))
    Emp_Name=input("Enter Employee Name : ")
    Job_Role=input("Enter Role of Employee : ")
    Hire_Date=input("Enter Joining Date : ")
    dept_no=int(input("Enter Dept No : "))
    Sal=float(input("Enter your Salary : "))
    records=[{
        "Emp NO" : Emp_no,
        "Emp Name" : Emp_Name,
        "Job":Job_Role,
        "Hire Date":Hire_Date,
        "Dept NO":dept_no,
        "Salary" : Sal
    }]
    information.insert_many(records)
    if i==n:
        break

information.insert_many(records)

class Employees:
    def __init__(self, name):
        self.name = name
        self.relationships = []

class Organization:
    def __init__(self, name):
        self.name = name

app = Flask(__name__)
@app.route('/api', methods=['GET'])
def api():
    data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }
    return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True)
