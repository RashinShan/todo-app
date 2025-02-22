from django.test import TestCase
from django.urls import reverse
from To_Do.models import Task

class TaskIntegrationTest(TestCase):

    def test_task_creation_and_marking_done(self):
        task = Task.objects.create(title="Test Task", description="Test Description")
        self.assertEqual(Task.objects.count(), 1)

        response = self.client.get(reverse('mark_done', args=[task.id]))
        task.refresh_from_db()
        self.assertTrue(task.completed)

    def test_add_and_view_task(self):
        data = {'title': 'New Task', 'description': 'New Description'}
        self.client.post(reverse('add_task'), data)
        
        response = self.client.get(reverse('task_list'))
        self.assertContains(response, "New Task")
