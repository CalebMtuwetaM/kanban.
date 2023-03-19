import unittest
import kanban


class TestKanban(unittest.TestCase):
    def test_create_task(self):
        self.assertTrue(kanban.tasks[0:2])


if __name__ == '__main__':
    unittest.main()
