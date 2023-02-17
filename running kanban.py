#This is the running of the kanban
import kanban
#creating a task
kanban.create_task("washing clothes ")
kanban.create_task("watching tv ")
kanban.create_task("doing homework ")
kanban.create_task("play basketball ")
kanban.create_task("go for interview ")
kanban.create_task("hack systems ")

task1 = kanban.tasks[0]
task2 = kanban.tasks[1]
task3 = kanban.tasks[2]
task4 = kanban.tasks[3]
task5 = kanban.tasks[4]
task6 = kanban.tasks[5]

#moving the task to doing state
kanban.move_to_doing(task1["task_id"])

#move a task to done state
kanban.move_to_done(task1["task_id"])

#listing tasks in todo state
kanban.list_todo()

#listing tasks in the doing state
kanban.list_doing()

#listing tasks in the done state
kanban.list_done()

#listing all tasks in all states 
kanban.show_all_tasks()
