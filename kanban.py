#import neccesary modules
import uuid
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
import os
import MySQLdb
import certifi
import os 
import mysql.connector






connection = MySQLdb.connect(
    host= os.getenv("hostname"),
    user= os.getenv("username"),
    passwd= os.getenv("password"),
    db= os.getenv("database"),
    ssl  = {
        "ssl_ca": "/etc/ssl/cert.pem"
    }
)


import mysql.connector

# Create a connection to the MySQL database
connection = mysql.connector.connect(
    host= os.getenv("hostname"),
    user= os.getenv("username"),
    password= os.getenv("password"),
    database= os.getenv("database")
   
)
cursor = connection.cursor()

def create_task(name):
    # Task name should not be empty
    if name is None:
        raise ValueError("Name cannot be None")

    # Task name should be unique
    cursor.execute("SELECT * FROM tasks WHERE task_name = %s", (name,))
    result = cursor.fetchone()
    if result is not None:
        raise ValueError("Task name should be unique")

    # Task properties
    task_id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = None
    state = "todo"

    # Insert task into database
    sql = "INSERT INTO tasks (task_id, task_name, created_at, updated_at, state) VALUES (%s, %s, %s, %s, %s)"
    val = (task_id, name, created_at, updated_at, state)
    cursor.execute(sql, val)
    connection.commit()

    # Retrieve inserted task from database
    cursor.execute("SELECT * FROM tasks WHERE task_id = %s", (task_id,))
    result = cursor.fetchone()

    task = {
        "task_id": result[0],
        "task_name": result[1],
        "created_at": result[2],
        "updated_at": result[3],
        "state": result[4]
    }

    return task



"""
#task list that is empty
tasks = []

#create task functionality
# Modify create_task function to return the created task object
def create_task(name):
    # Task name should not be empty

    is_created = False

    if name is None:
        raise ValueError("Name cannot be None")
    # rest of the function logic

    # Task name should be unique
    for task in tasks:
        if task["task_name"] == name:
            raise ValueError("Task name should be unique")

    # Task properties
    task = {
        "task_id" : str(uuid.uuid4()),
        "task_name" : name,
        "created_at" : datetime.now(),
        "updated_at" : None,
        "state" : "todo"
    }

    tasks.append(task)
    is_created = True
    if is_created == False:
        raise ValueError("Task was not created")
    return None

"""




def move_to_todo(task_id):
    is_moved = False
    for task in tasks:
        if task["task_id"] == task_id and task["state"] != "todo":
            task["state"] = "todo"
            is_moved = True

    if is_moved == False:
        raise ValueError("The task_id does not exist")

#move the task to doing state
def move_to_doing(task_id):
    is_moving = False
    for task in tasks:
        if task["task_id"] == task_id and task["state"] != "doing":
            task["state"] = "doing"
            task["updated_at"] = datetime.now()
            is_moving = True

    if is_moving == False:
        raise ValueError("The task_id does not exist")

#move the task to done state

def move_to_done(task_id):
    is_done = False
    for task in tasks:
        if task["task_id"] == task_id and task["state"] != "done":
            task["state"] = "done"
            is_done = True

    if is_done == False:
        raise ValueError ("The task_id does not exist")

#list the todo tasks
def list_todo():
    todo_list = []
    for task in tasks:
        if task["state"] == "todo":
            todo_list.append(task)
    return todo_list

#list doing tasks
def list_doing():
    doing_list = []
    for task in tasks:
        if task["state"] == "doing":
            doing_list.append(task)
    return doing_list

#list done tasks
def list_done():
    done_list = []
    for task in tasks:
        if task["state"] == "done":
            done_list.append(task)
    return done_list

#list all tasks
def show_all_tasks():
    return tasks

import update_run

