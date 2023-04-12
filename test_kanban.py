import unittest
import kanban
from kanban import tasks
class Testkanban(unittest.TestCase):

    # test for the create_task function

    def test_create_task(self):
        is_created = False
        kanban.create_task("Task2")
        Task2 = kanban.tasks[0]
        for task in tasks:
            if task["task_name"] == "Task2":
                is_created = True
        if is_created == False:
            self.assertRaises(ValueError)

    def test_for_name(self):
        with self.assertRaises(ValueError):
            kanban.create_task(None)


    def test_if_name_is_unique(self):
        # Create a task with a unique name
        task1 = kanban.create_task("task1")

        # Try to create a task with the same name, should raise an error
        with self.assertRaises(ValueError):
            kanban.create_task("task1")

    # test for move_to_doing function

    def test_move_to_doing(self):
        # try to move a task with an unexisting task_id
        with self.assertRaises(ValueError):
            kanban.move_to_doing("invalid_id")
        # to test if the user has passed in a task_id
        with self.assertRaises(ValueError):
            kanban.move_to_doing(None)


    def test_move_to_doing_functionality(self):
        # Create a task with known task ID and initial state


        kanban.create_task("Task1")
        Task1 = kanban.tasks[0]
        is_moved = False
        # Move the task to "doing" state
        kanban.move_to_doing(Task1["task_id"])
        is_moved = True
        if is_moved == False:
            self.assertRaises(ValueError)

        # test for move_to_done function

    def test_move_to_done(self):
        # try to move a task with an unexisting task_id
        with self.assertRaises(ValueError):
            kanban.move_to_done("invalid_id")
        # to test if the user has passed in a task_id
        with self.assertRaises(ValueError):
            kanban.move_to_done(None)

    def test_move_to_done_functionality(self):
        # Create a task with known task ID and initial state

        kanban.create_task("Task4")
        Task4 = kanban.tasks[0]
        is_moved = False
        # Move the task to "doing" state
        kanban.move_to_done(Task4["task_id"])
        is_moved = True
        if is_moved == False:
            self.assertRaises(ValueError)





if __name__ == '__main__':
    unittest.main()
