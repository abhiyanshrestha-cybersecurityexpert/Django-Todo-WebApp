from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.

def home(request):
    todo_objs = Todo.objects.all() # Runs all the query from the todo table
    data = {'todos': todo_objs} # Send file from data variable as support 
    return render(request,'index.html',context=data)

def create(request):
    # data create request
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        
        Todo.objects.create(name=name,description=description,status=status) # running query orm
        return redirect('home')
    return render(request,'create.html')

def edit(request,pk):
    todo = Todo.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        todo.name = name
        todo.description = description
        todo.status = status
        todo.save()
        
        return redirect('home')
    data = {'todo': todo}
    return render(request,'edit.html',context=data)

def delete(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('home')
    
