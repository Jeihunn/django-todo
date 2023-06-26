from django.http import HttpResponseForbidden, JsonResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import List, Todo, Favorite
from .forms import ListForm, TodoForm, TodoDetailForm


# ========== List ==========

@login_required(login_url="account:login_view")
def list_view(request):
    todo_lists = List.objects.filter(
        is_active=True, user=request.user).order_by("-updated_at")

    form = ListForm()

    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            todo_list = List.objects.create(title=title, user=request.user)
            return redirect("todo:list_view")

    for list_item in todo_lists:
        list_item.todos_count = list_item.list_todos.filter(
            is_active=True, is_deleted=False).count()

    context = {
        "todo_lists": todo_lists,
        "form": form,
    }
    return render(request, "todo/list.html", context)


@login_required(login_url="account:login_view")
def list_delete_view(request, list_slug):
    todo_list = get_object_or_404(List, slug=list_slug)

    if todo_list.user != request.user:
        return HttpResponseForbidden("Bu listə icazəniz yoxdur.")

    todo_list.delete()
    messages.success(request, f"Siyahı '{todo_list.title}' silindi!")
    return redirect(request.META.get('HTTP_REFERER', 'todo:list_view'))

# ========== END List ==========


# ========== Todo ==========

@login_required(login_url="account:login_view")
def todo_view(request, list_slug):
    todo_list = get_object_or_404(List, slug=list_slug)

    if todo_list.user != request.user:
        return HttpResponseForbidden("Bu listə icazəniz yoxdur.")

    todos = Todo.objects.filter(
        is_active=True, is_deleted=False, user=request.user, list=todo_list).order_by("-updated_at")
    favorites = todos.filter(favorites__user=request.user)
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            todo = Todo.objects.create(
                title=title, user=request.user, list=todo_list)
            return redirect("todo:todo_view", list_slug=list_slug)

    context = {
        "todo_list": todo_list,
        "todos": todos,
        "favorites": favorites,
        "form": form,
    }
    return render(request, "todo/todo.html", context)


@login_required(login_url="account:login_view")
def toggle_completed_view(request, list_slug, todo_slug):
    todo = get_object_or_404(Todo, list__slug=list_slug, slug=todo_slug)

    if todo.is_deleted:
        raise Http404("Bu tapşırıq silinib.")

    if todo.user != request.user:
        return HttpResponseForbidden("Bu tapşırığa icazəniz yoxdur.")

    todo.is_completed = not todo.is_completed
    todo.save()
    return JsonResponse({'success': True})


@login_required(login_url="account:login_view")
def todo_completed_view(request, list_slug):
    todo_list = get_object_or_404(List, slug=list_slug)

    if todo_list.user != request.user:
        return HttpResponseForbidden("Bu listə icazəniz yoxdur.")

    todos = Todo.objects.filter(
        is_active=True, is_deleted=False, user=request.user, list__slug=list_slug, is_completed=True).order_by("-updated_at")
    favorites = todos.filter(favorites__user=request.user)
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            todo = Todo.objects.create(
                title=title, user=request.user, list=todo_list)
            return redirect("todo:todo_view", list_slug=list_slug)

    context = {
        "todo_list": todo_list,
        "todos": todos,
        "favorites": favorites,
        "form": form,
    }
    return render(request, "todo/todo.html", context)


@login_required(login_url="account:login_view")
def todo_uncompleted_view(request, list_slug):
    todo_list = get_object_or_404(List, slug=list_slug)

    if todo_list.user != request.user:
        return HttpResponseForbidden("Bu listə icazəniz yoxdur.")

    todos = Todo.objects.filter(
        is_active=True, is_deleted=False, user=request.user, list__slug=list_slug, is_completed=False).order_by("-updated_at")
    favorites = todos.filter(favorites__user=request.user)
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            todo = Todo.objects.create(
                title=title, user=request.user, list=todo_list)
            return redirect("todo:todo_view", list_slug=list_slug)

    context = {
        "todo_list": todo_list,
        "todos": todos,
        "favorites": favorites,
        "form": form,
    }
    return render(request, "todo/todo.html", context)


@login_required(login_url="account:login_view")
def todo_favorited_view(request, list_slug):
    todo_list = get_object_or_404(List, slug=list_slug)

    if todo_list.user != request.user:
        return HttpResponseForbidden("Bu listə icazəniz yoxdur.")

    todos = Todo.objects.filter(
        favorites__user=request.user, is_active=True, list__slug=list_slug, is_deleted=False,).order_by("-updated_at")
    favorites = todos.filter(favorites__user=request.user)
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            todo = Todo.objects.create(
                title=title, user=request.user, list=todo_list)
            return redirect("todo:todo_view", list_slug=list_slug)

    context = {
        "todo_list": todo_list,
        "todos": todos,
        "favorites": favorites,
        "form": form,
    }
    return render(request, "todo/todo.html", context)


@login_required(login_url="account:login_view")
def add_favorite_view(request, list_slug, todo_slug):
    todo = get_object_or_404(Todo, list__slug=list_slug, slug=todo_slug)

    if todo.is_deleted:
        raise Http404("Bu tapşırıq silinib.")

    if todo.user != request.user:
        return HttpResponseForbidden("Bu tapşırığa icazəniz yoxdur.")

    try:
        favorite = request.user.favorited_by
    except Favorite.DoesNotExist:
        favorite = Favorite.objects.create(user=request.user)

    favorite.add_todo_to_favorites(todo)
    return redirect(request.META.get('HTTP_REFERER', 'todo:todo_view'))


@login_required(login_url="account:login_view")
def remove_favorite_view(request, list_slug, todo_slug):
    todo = get_object_or_404(Todo, list__slug=list_slug, slug=todo_slug)

    if todo.is_deleted:
        raise Http404("Bu tapşırıq silinib.")

    if todo.user != request.user:
        return HttpResponseForbidden("Bu tapşırığa icazəniz yoxdur.")

    request.user.favorited_by.remove_todo_from_favorites(todo)
    return redirect(request.META.get('HTTP_REFERER', 'todo:todo_view'))


@login_required(login_url="account:login_view")
def todo_update_view(request, list_slug, todo_slug):
    todo_list = get_object_or_404(List, slug=list_slug)
    todo = get_object_or_404(Todo, list__slug=list_slug, slug=todo_slug)

    if todo.is_deleted:
        raise Http404("Bu tapşırıq silinib.")

    if todo.user != request.user:
        return HttpResponseForbidden("Bu tapşırığa icazəniz yoxdur.")

    form = TodoDetailForm(instance=todo)

    if request.method == "POST":
        form = TodoDetailForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, "Məlumatlar uğurla dəyişdirildi.")
            return redirect("todo:todo_view", list_slug=list_slug)

    context = {
        "todo_list": todo_list,
        "todo": todo,
        "form": form,
    }
    return render(request, "todo/update.html", context)


@login_required(login_url="account:login_view")
def todo_detail_view(request, list_slug, todo_slug):
    todo_list = get_object_or_404(List, slug=list_slug)
    todo = get_object_or_404(Todo, list__slug=list_slug, slug=todo_slug)

    if todo.is_deleted:
        raise Http404("Bu tapşırıq silinib.")

    if todo.user != request.user:
        return HttpResponseForbidden("Bu tapşırığa icazəniz yoxdur.")

    is_favorite = Favorite.objects.filter(
        user=request.user, todos__id=todo.id).exists()

    context = {
        "todo_list": todo_list,
        "todo": todo,
        "is_favorite": is_favorite,
    }
    return render(request, "todo/detail.html", context)


@login_required(login_url="account:login_view")
def todo_delete_view(request, list_slug, todo_slug):
    todo = get_object_or_404(Todo, list__slug=list_slug, slug=todo_slug)

    if todo.user != request.user:
        return HttpResponseForbidden("Bu tapşırığa icazəniz yoxdur.")

    todo.is_deleted = True
    todo.save()
    messages.success(
        request, f"Tapşırıq '{todo.title}' zibil qutusuna köçürüldü.")

    return redirect(request.META.get('HTTP_REFERER', 'todo:todo_view'))


@login_required(login_url="account:login_view")
def todo_delete_all_view(request, list_slug):
    todos = Todo.objects.filter(
        is_active=True, user=request.user, list__slug=list_slug)
    todos.update(is_deleted=True)
    messages.success(
        request, "Bütün tapşırıqlar zibil qutusuna köçürüldü.")
    return redirect(request.META.get('HTTP_REFERER', 'todo:todo_view'))

# ========== END Todo ==========


# # =============== Trash ===============

@login_required(login_url="account:login_view")
def trash_view(request):
    deleted_todos = Todo.objects.filter(
        is_active=True, is_deleted=True, user=request.user).order_by("-updated_at")
    context = {
        "deleted_todos": deleted_todos,
    }
    return render(request, 'todo/trash.html', context)


@login_required(login_url="account:login_view")
def restore_todo_view(request, todo_slug):
    todo = get_object_or_404(Todo, slug=todo_slug)
    todo.is_deleted = False
    todo.save()
    messages.success(
        request, f"Tapşırıq '{todo.title}' uğurla bərpa edildi.")
    return redirect('todo:trash_view')


@login_required(login_url="account:login_view")
def permanently_delete_todo_view(request, todo_slug):
    todo = get_object_or_404(Todo, slug=todo_slug)
    messages.success(
        request, f"Tapşırıq '{todo.title}' həmişəlik silindi.")
    todo.delete()
    return redirect('todo:trash_view')


@login_required(login_url="account:login_view")
def empty_trash_view(request):
    deleted_todos = Todo.objects.filter(
        is_active=True, is_deleted=True, user=request.user)
    deleted_todos.delete()
    messages.success(
        request, "Zibil qutusu boşaltıldı!")
    return redirect('todo:trash_view')

# # =============== END Trash ===============
