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
kanban.move_to_doing(task2["task_id"])
kanban.move_to_doing(task3["task_id"])
kanban.move_to_doing(task4["task_id"])
kanban.move_to_doing(task5["task_id"])
kanban.move_to_doing(task6["task_id"])

print(kanban.tasks)
#showing all the tasks in all states
kanban.show_all_tasks()