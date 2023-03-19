import unittest
import kanban


class TestKanban(unittest.TestCase):
    def test_create_task(self):
        self.assertTrue(kanban.tasks[0:2])

    def  test_for_name(self):
        self.assertIsNone(kanban.create_task("name"))

if __name__ == '__main__':
    unittest.main()
