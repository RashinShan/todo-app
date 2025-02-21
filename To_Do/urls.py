from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name="task_list"),
    path('add/', views.add_task, name="add_task"),
    path('done/<int:task_id>/', views.mark_done, name="mark_done"),
]
