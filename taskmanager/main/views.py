from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.

def index(request):
    tasks = Task.objects.all().order_by('-id') #обратная сортировка от нового к старому # [:5] ограничение по  количеству записей на странице
    return render(request, 'main/index.html', {'title':'Main page site', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')    


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error='incorrect forms'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)  