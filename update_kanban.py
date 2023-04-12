#import neccesary modules
import uuid
from datetime import datetime

#task list that is empty
tasks = []

#create task functionality
def create_task(name):
    #task name should not be empty
    if name == "":
        raise("task name should not be empty")

    #task name should be unique
    for task in tasks:
        if ["name"] == name:
            raise("task name should be unique")

    #task properties
    task = {
        "task_id" : str(uuid.uuid4()),
        "task_name" : name,
        "created_at" : datetime.now(),
        "updated_at" : None,
        "state" : "todo"
    }

    tasks.append(task)

#to find a task with task id
def find_task_by_ID(task_id):
    is_found = False
    for task in tasks:
        if task["task_id"] == task_id:
            task_ = task
            is_found = True
            break
    return is_found,task_

def move_to_todo(task_id):
    is_moved = False
    is_found,task_ = find_task_by_ID(task_id)
    if not is_found:
        raise("task with task id not found")
    if task_["state"] != "todo":
        task_["state"] = "todo"
    is_moved = True

    if is_moved == False:
        raise("task_id" + task_id + "is not existing")

#move the task to doing state
def move_to_doing(task_id):
    is_moving = False
    is_found,task_ = find_task_by_ID(task_id)
    if not is_found:
        raise("the task with task id not found")
    if task_["state"] != "doing":
        task_["state"] = "doing"
    is_moving = True

    if is_moving == False:
        raise("task_id" + task_id + "does not exist")

#move the task to done state

def move_to_done(task_id):
    is_done = False
    is_found,task_ = find_task_by_ID(task_id)
    if not is_found:
        raise("the task with task id was not found")
    if task_["state"] != "done":
        task_["state"] = "done"
    is_done = True

    if is_done == False:
        raise("task_id" + task_id + "does not exist")

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
