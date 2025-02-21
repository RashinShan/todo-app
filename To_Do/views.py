from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.filter(completed=False)
    return render(request, 'todo/index.html', {"tasks": tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")

        if title and description:  # Ensure data is valid
            Task.objects.create(title=title, description=description)

        return redirect("task_list")  # Redirect after adding

    return render(request, "todo/index.html")

def mark_done(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect("task_list")
