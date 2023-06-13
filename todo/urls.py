from django.urls import path
from . import views

app_name = "todo"
urlpatterns = [
    path('', views.index_view, name="index_view"),
    path('todo/update/<slug:todo_slug>/', views.update_view, name="update_view"),
    path('todo/delete/<slug:todo_slug>/', views.delete_view, name="delete_view"),
    path('todo/completed/', views.todo_completed_view, name="todo_completed_view"),
    path('todo/uncompleted/', views.todo_uncompleted_view, name="todo_uncompleted_view"),
    path('toggle-completed/<slug:todo_slug>/', views.toggle_completed, name='toggle_completed'),

]
