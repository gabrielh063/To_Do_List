import unittest
import backend.controllers.task_controller as task


class Testtask(unittest.TestCase):
    def test_add_task(self):
        # Assuming add_task(title, description) returns a dict with task info
        result = task.add_task("Test Task", "Test Description")
        self.assertIn("id", result)
        self.assertEqual(result["title"], "Test Task")
        self.assertEqual(result["description"], "Test Description")

    def test_get_task(self):
        # Assuming get_task(id) returns a dict with task info
        new_task = task.add_task("Another Task", "Another Description")
        task_id = new_task["id"]
        result = task.get_task(task_id)
        self.assertEqual(result["id"], task_id)
        self.assertEqual(result["title"], "Another Task")

    def test_update_task(self):
        # Assuming update_task(id, title, description) updates and returns the task
        new_task = task.add_task("Update Task", "Old Description")
        task_id = new_task["id"]
        updated = task.update_task(task_id, "Updated Task", "New Description")
        self.assertEqual(updated["title"], "Updated Task")
        self.assertEqual(updated["description"], "New Description")

    def test_delete_task(self):
        # Assuming delete_task(id) returns True if deleted
        new_task = task.add_task("Delete Task", "To be deleted")
        task_id = new_task["id"]
        result = task.delete_task(task_id)
        self.assertTrue(result)
        # Optionally, check that get_task now fails or returns None
        self.assertIsNone(task.get_task(task_id))

if __name__ == "__main__":
    unittest.main()