from django.shortcuts import render, redirect, get_object_or_404
from .models import Register, Task
from .forms import TaskForm, UpdateTaskForm


def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        # Retrieve form data from the POST request
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Perform basic validation (you may want to add more thorough validation)
        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Passwords do not match'})

        # Create a new Register instance and save it to the database
        new_user = Register(username=username, password=password, confirm_password=confirm_password)
        new_user.save()

        # Redirect to the login page after successful registration
        return redirect('login')

        # If the request method is not POST, just render the registration page
    return render(request, 'register.html')


def task(request):
    context = {'success': False}
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        todo = Task(title=title, description=desc)
        todo.save()
        context = {'success': True}
        return render(request, 'task.html', context)
    return render(request, 'task.html')


def task_list(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')

    return render(request, 'task_list.html', {'tasks': tasks, 'form': form})
#
#
# def update_task(request, task_id):
#     task = get_object_or_404(Task, pk=task_id)
#     form = UpdateTaskForm(instance=task)
#
#     if request.method == 'POST':
#         form = UpdateTaskForm(request.POST, instance=task)
#         if form.is_valid():
#             form.save()
#             return redirect('task_list')
#
#     return render(request, 'update_task.html', {'form': form})


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return render(request, 'delete_task.html', {'task': task})


def lg_out(request):
    return redirect('login')
