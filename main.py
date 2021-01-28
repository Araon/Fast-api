from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


api = FastAPI()

# temp database
fakedb = []

# todolist model to store tasks
class task(BaseModel):
    id: int
    name: str
    is_urgent: Optional[bool] = None

# Home/welcome route
@api.get("/")
def read_root():
    return {"Data": "Hello world"}

# Get all task
@api.get("/tasks")
def get_task():
    return fakedb

# get single task
@api.get("/tasks/{task_id}")
def get_a_task(task_id: int):
    todo = task_id - 1
    return fakedb[todo]

# add a new task
@api.post("/addtask")
def add_task(course: task):
    fakedb.append(course.dict())
    return {"Data":"Task Added"}

# delete a task
@api.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    fakedb.pop(task_id-1)
    return {"Data": "Deletion successful"}
