#This is the running of the kanban
import kanban

#creating a task
#kanban.create_task("pray ")
"""kanban.create_task("watching tv ")
kanban.create_task("doing homework ")
kanban.create_task("play basketball ")
kanban.create_task("go for interview ")
kanban.create_task("hack systems ")"""


#

"""task2 = kanban.tasks[1]
task3 = kanban.tasks[2]
task4 = kanban.tasks[3]
task5 = kanban.tasks[4]
task6 = kanban.tasks[5]
"""

#to test if the function that finds a task by task id really works
#print(kanban.find_task_by_ID(task1["task_id"]))

#moving the task to doing state
#print(kanban.move_to_doing(task1["task_id"]))

#move a task to done state
#print(kanban.move_to_done(task1["task_id"]))

#listing tasks in todo state
#print(kanban.list_todo())

#listing tasks in the doing state
#print(kanban.list_doing())

#listing tasks in the done state
#print(kanban.list_done())

#listing all tasks in all states
#print(kanban.show_all_tasks())

"""
import sqlite3

def import_tasks_from_database():
    # connect to the database
    conn = sqlite3.connect('my_database.db')
    c = conn.cursor()
    
    # execute a SELECT query to retrieve all tasks
    c.execute('SELECT * FROM tasks')
    rows = c.fetchall()
    
    # create a list of tasks
    tasks = []
    for row in rows:
        task = {
            'task_id': row[0],
            'description': row[1],
            'state': row[2],
            'created_at': row[3]
        }
        tasks.append(task)
    
    # close the database connection
    conn.close()
    
    return tasks


    task1 = kanban.tasks[0]



import_tasks_from_database()"""