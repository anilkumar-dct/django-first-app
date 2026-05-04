from django.shortcuts import render

from .models import Todo

# Create your views here.
def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = request.POST.get('completed') == 'on'
        todos = Todo.objects.create(title=title, description=description, completed=completed)
        # Here you would typically save the todo to the database
        return list_todos(request)
    return render(request, 'create_todo.html')

def list_todos(request):
    todos = Todo.objects.all()
    return render(request, 'list_todo.html', {'todos': todos})

def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.completed = request.POST.get('completed') == 'on'
        todo.save()
        return list_todos(request)
    return render(request, 'update_todo.html', {'todo': todo})

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.delete()
        return list_todos(request)
    return render(request, 'delete_todo.html', {'todo': todo})