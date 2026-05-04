
from .views import create_todo, list_todos, update_todo, delete_todo
from django.urls import path

urlpatterns = [
    path('create_todo/', create_todo, name='create_todo'),
    path('list_todos/', list_todos, name='list_todos'),
    path('update_todo/<int:todo_id>/', update_todo, name='update_todo'),
    path('delete_todo/<int:todo_id>/', delete_todo, name='delete_todo'),
]