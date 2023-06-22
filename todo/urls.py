from django.urls import path
from . import views

app_name = "todo"
urlpatterns = [
    # List
    path('', views.list_view, name="list_view"),
    # List Delete
    path('list/<slug:list_slug>/delete', views.list_delete_view, name="list_delete_view"),

    # TO-DO Filter
    path('list/<slug:list_slug>/todos/', views.todo_view, name="todo_view"),
    path('list/<slug:list_slug>/todos/completed/', views.todo_completed_view, name="todo_completed_view"),
    path('list/<slug:list_slug>/todos/uncompleted/', views.todo_uncompleted_view, name="todo_uncompleted_view"),
    path('list/<slug:list_slug>/todos/favorited/', views.todo_favorited_view, name="todo_favorited_view"),
    # TO-DO Toggle-Comleted
    path('toggle-completed/<slug:list_slug>/<slug:todo_slug>/', views.toggle_completed_view, name='toggle_completed_view'),
    # TO-DO Favorite
    path('list/<slug:list_slug>/todo/<slug:todo_slug>/add-favorite/', views.add_favorite_view, name="add_favorite_view"),
    path('list/<slug:list_slug>/todo/<slug:todo_slug>/remove-favorite/', views.remove_favorite_view, name="remove_favorite_view"),
    # TO-DO Update
    path('list/<slug:list_slug>/todo/<slug:todo_slug>/update/', views.todo_update_view, name="todo_update_view"),
    # TO-DO Delete
    path('list/<slug:list_slug>/todo/<slug:todo_slug>/delete/', views.todo_delete_view, name="todo_delete_view"),
    path('list/<slug:list_slug>/todos/delete-all', views.todo_delete_all_view, name="todo_delete_all_view"),
    # TO-DO Detail
    path('list/<slug:list_slug>/todo/<slug:todo_slug>/', views.todo_detail_view, name="todo_detail_view"),
    # Trash
    path('trash/', views.trash_view, name="trash_view"),
    path('trash/todo/<slug:todo_slug>/restore/', views.restore_todo_view, name="restore_todo_view"),
    path('trash/todo/<slug:todo_slug>/permanently-delete/', views.permanently_delete_todo_view, name="permanently_delete_todo_view"),
    path('empty-trash/', views.empty_trash_view, name="empty_trash_view"),
]
