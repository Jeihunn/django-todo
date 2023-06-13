from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm, TodoDetailForm


@login_required(login_url="account:login_view")
def index_view(request):
    todos = Todo.objects.filter(
        is_active=True, user=request.user).order_by("-updated_at")
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            todo = Todo.objects.create(title=title, user=request.user)
            return redirect("todo:index_view")

    context = {
        "todos": todos,
        "form": form,
    }
    return render(request, "todo/index.html", context)


@login_required(login_url="account:login_view")
def update_view(request, todo_slug):
    todo = get_object_or_404(Todo, slug=todo_slug)
    form = TodoDetailForm(instance=todo)

    if request.method == "POST":
        form = TodoDetailForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todo:index_view")

    context = {
        "todo": todo,
        "form": form,
    }
    return render(request, "todo/update.html", context)


@login_required(login_url="account:login_view")
def delete_view(request, todo_slug):
    todo = get_object_or_404(Todo, slug=todo_slug)
    todo.delete()
    return redirect(request.META.get('HTTP_REFERER', 'todo:index_view'))


@login_required(login_url="account:login_view")
def todo_completed_view(request):
    todos = Todo.objects.filter(
        is_active=True, user=request.user, is_completed=True).order_by("-updated_at")
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            todo = Todo.objects.create(title=title, user=request.user)
            return redirect("todo:index_view")

    context = {
        "todos": todos,
        "form": form,
    }
    return render(request, "todo/index.html", context)


@login_required(login_url="account:login_view")
def todo_uncompleted_view(request):
    todos = Todo.objects.filter(
        is_active=True, user=request.user, is_completed=False).order_by("-updated_at")
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            todo = Todo.objects.create(title=title, user=request.user)
            return redirect("todo:index_view")

    context = {
        "todos": todos,
        "form": form,
    }
    return render(request, "todo/index.html", context)


@login_required(login_url="account:login_view")
def toggle_completed(request, todo_slug):
    todo = get_object_or_404(Todo, slug=todo_slug)
    todo.is_completed = not todo.is_completed
    todo.save()
    return JsonResponse({'success': True})
