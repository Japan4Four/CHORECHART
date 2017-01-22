from django.http import HttpResponse

from .models import Task

def index(request):
    return HttpResponse("Hello, world. You're at the TASKS index.")

def task_list(request):
    available_tasks = Task.objects.order_by('-priority')
    template = loader.get_template('tasks\index.html')
    context = {
        'available_tasks' : available_tasks,
        }
    return HttpResponse(template.render(context,request))

