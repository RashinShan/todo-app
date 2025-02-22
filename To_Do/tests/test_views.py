from django.test import TestCase
from django.urls import reverse
from To_Do.models import Task

class TaskViewsTest(TestCase):

    def test_add_task_view(self):
        data = {'title': 'New Task', 'description': 'New Description'}
        response = self.client.post(reverse('add_task'), data)
        self.assertEqual(response.status_code, 302)  # Assuming a redirect happens after task creation
        self.assertTrue(Task.objects.filter(title="New Task").exists())

    def test_mark_done_view(self):
        task = Task.objects.create(title="Test Task", description="Test Description")
        response = self.client.get(reverse('mark_done', args=[task.id]))
        task.refresh_from_db()
        self.assertTrue(task.completed)

    def test_task_list_view(self):
        Task.objects.create(title="Test Task 1", description="Test Description 1")
        Task.objects.create(title="Test Task 2", description="Test Description 2")
        
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task 1")
        self.assertContains(response, "Test Task 2")
