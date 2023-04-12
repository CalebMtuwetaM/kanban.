import unittest
import kanban

class Testkanban(unittest.TestCase):
    def test_create_task(self):
        self.assertTrue(kanban.tasks[0:5])

    def test_for_name(self):
        with self.assertRaises(ValueError):
            kanban.create_task(None)


    def test_if_name_is_unique(self):
        # Create a task with a unique name
        task1 = kanban.create_task("task1")

        # Try to create a task with the same name, should raise an error
        with self.assertRaises(ValueError):
            kanban.create_task("task1")


if __name__ == '__main__':
    unittest.main()
