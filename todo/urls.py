from django.urls import path
from . import views

app_name = "todo"
urlpatterns = [
    path('', views.index_view, name="index_view"),
    path('todos/completed/', views.todo_completed_view, name="todo_completed_view"),
    path('todos/uncompleted/', views.todo_uncompleted_view, name="todo_uncompleted_view"),
    path('todos/favorited/', views.todo_favorited_view, name="todo_favorited_view"),
    path('todo/update/<slug:todo_slug>/', views.update_view, name="update_view"),

    # delete
    path('todo/delete/<slug:todo_slug>/', views.delete_view, name="delete_view"),
    path('todo/delete/delete-all', views.delete_all_view, name="delete_all_view"),

    # trash
    path('trash/', views.trash_view, name="trash_view"),
    path('trash/todo/restore/<slug:todo_slug>/', views.restore_todo_view, name="restore_todo_view"),
    path('trash/todo/permanently-delete/<slug:todo_slug>/', views.permanently_delete_todo_view, name="permanently_delete_todo_view"),
    path('empty-trash/', views.empty_trash_view, name="empty_trash_view"),

    path('todo/<slug:todo_slug>/', views.detail_view, name="detail_view"),
    path('todo/add-favorite/<slug:todo_slug>/', views.add_favorite_view, name="add_favorite_view"),
    path('todo/remove-favorite/<slug:todo_slug>/', views.remove_favorite_view, name="remove_favorite_view"),
    path('toggle-completed/<slug:todo_slug>/', views.toggle_completed, name='toggle_completed'),

]
