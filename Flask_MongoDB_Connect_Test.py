import pymongo
client = pymongo.MongoClient('mongodb+srv://naveenchandgadde:ChanduG97@flask.0zcjxbr.mongodb.net/')
mydb = client['Employee']
information=mydb.table1
records = [{

        "Emp NO" : 501,
        "Emp Name":"Chandu",
        "Job":"Associate Software Engineer",
        "Hire Date":"03-07-2023",
        "Dept NO":2,
        "Salary" : 15000
    }]
information.insert_many(records)

class Object1:
    def __init__(self, name):
        self.name = name
        self.relationships = []

class Object2:
    def __init__(self, name):
        self.name = name