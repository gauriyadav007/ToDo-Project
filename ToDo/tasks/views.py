from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.contrib import messages


@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user, is_deleted=False).order_by('-created_at')
    return render(request, 'home.html', {'tasks': tasks})


def about(request):
    return render(request, 'about.html')


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            t = form.save(commit=False)
            t.user = request.user
            t.save()
            messages.success(request, 'Task added successfully.')
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})


@login_required
def update_task(request, pk):
    try:
        task = Task.objects.get(pk=pk, user=request.user)
    except Task.DoesNotExist:
        messages.error(request, 'Task not found.')
        return redirect('home')

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'update_task.html', {'form': form, 'task': task})


@login_required
def delete_task(request, pk):
    try:
        task = Task.objects.get(pk=pk, user=request.user)
        task.is_deleted = True
        task.save()
        messages.success(request, 'Task moved to Trash!')
    except Task.DoesNotExist:
        messages.error(request, 'Task not found.')
    return redirect('home')


@login_required
def trash(request):
    deleted = Task.objects.filter(user=request.user, is_deleted=True).order_by('-created_at')
    return render(request, 'trash.html', {'deleted': deleted})


@login_required
def restore_task(request, pk):
    try:
        task = Task.objects.get(pk=pk, user=request.user, is_deleted=True)
        task.is_deleted = False
        task.save()
        messages.success(request, 'Task restored successfully!')
    except Task.DoesNotExist:
        messages.error(request, 'Task not found.')
    return redirect('trash')


@login_required
def permanent_delete(request, pk):
    try:
        task = Task.objects.get(pk=pk, user=request.user, is_deleted=True)
        task.delete()
        messages.success(request, 'Task deleted permanently!')
    except Task.DoesNotExist:
        messages.error(request, 'Task not found.')
    return redirect('trash')


@login_required
def restore_all(request):
    Task.objects.filter(user=request.user, is_deleted=True).update(is_deleted=False)
    messages.success(request, 'All tasks restored.')
    return redirect('trash')


@login_required
def permanent_delete_all(request):
    Task.objects.filter(user=request.user, is_deleted=True).delete()
    messages.success(request, 'All tasks permanently deleted.')
    return redirect('trash')
