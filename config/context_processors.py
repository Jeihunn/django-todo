from todo.models import Todo


def trash_todo_count_global(request):
    if request.user.is_authenticated:
        trash_todo_count_global = Todo.objects.filter(
            user=request.user, is_deleted=True, is_active=True).count()
    else:
        trash_todo_count_global = 0

    return {
        'trash_todo_count_global': trash_todo_count_global
    }
