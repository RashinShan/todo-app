from django.test import TestCase
from To_Do.models import Task

class TaskModelTest(TestCase):

    def test_task_creation(self):
        task = Task.objects.create(title="Test Task", description="Test Description")
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertFalse(task.completed)  # Assuming 'completed' is False by default

    def test_task_title_uniqueness(self):
        Task.objects.create(title="Unique Task", description="Description for first task")
        with self.assertRaises(Exception):
            Task.objects.create(title="Unique Task", description="Description for second task")

    def test_str_method(self):
        task = Task.objects.create(title="Test Task", description="Test Description")
        self.assertEqual(str(task), "Test Task")  # Assuming `__str__` returns the title
