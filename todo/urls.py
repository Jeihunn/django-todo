from django.urls import path
from . import views

app_name = "todo"
urlpatterns = [
    path('', views.index_view, name="index_view"),
    path('todo/completed/', views.todo_completed_view, name="todo_completed_view"),
    path('todo/uncompleted/', views.todo_uncompleted_view, name="todo_uncompleted_view"),
    path('todo/favorited/', views.todo_favorited_view, name="todo_favorited_view"),
    path('todo/update/<slug:todo_slug>/', views.update_view, name="update_view"),
    path('todo/delete/<slug:todo_slug>/', views.delete_view, name="delete_view"),
    path('todo/<slug:todo_slug>/', views.detail_view, name="detail_view"),
    path('todo/add_favorite/<slug:todo_slug>/', views.add_favorite_view, name="add_favorite_view"),
    path('todo/remove_favorite/<slug:todo_slug>/', views.remove_favorite_view, name="remove_favorite_view"),
    path('toggle-completed/<slug:todo_slug>/', views.toggle_completed, name='toggle_completed'),

]
