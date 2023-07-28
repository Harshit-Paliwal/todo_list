from fastapi import FastAPI
from pydantic import BaseModel
from database import tasks
from pymongo import MongoClient

connection_string = "mongodb+srv://harshitpaliwal:Pb7vjsxxSOt0qVaj@infinix.ts2rbmw.mongodb.net/"
mongo_db = MongoClient(connection_string)
database = mongo_db.todolist
collection = database.tasks

task_obj = tasks(collection)

class addTASK(BaseModel):
    task_no:str
    task_name:str
    task_brief:str
    

    
app = FastAPI()

@app.post("/addTASK")
def addtask (json:addTASK):
    insert = task_obj.add_task(json.task_no,json.task_name,json.task_brief)
    return{"Task Added":insert}

@app.get("/task_name")
def fetch_task_name(task_no):
        data = collection.find_one({"task_no":task_no})
        return data["task_name"]
    
@app.get("/task_brief")
def fetch_task_brief(task_name):
        data = collection.find_one({"task_name":task_name})
        return data["task_brief"]
    
@app.get("/task_brief_using_task_no")
def fetch_task_brief_by_task_no(task_no):
        data = collection.find_one({"task_no":task_no})
        return data["task_brief"]