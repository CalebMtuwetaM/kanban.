#import neccesary modules
import uuid
from datetime import datetime

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

