from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the TASKS index.")

def task_list(request):
    return HttpResponse (" This is the task list")
