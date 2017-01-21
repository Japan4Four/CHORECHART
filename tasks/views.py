from django.http import HttpResponse


def index(request):
    # Eventually you will want to add a link in the html response to direct to /task_list
    # This link could be in the tasks index or project index.
    return HttpResponse("Hello, world. You're at the TASKS index.")

def task_list(request):
    return HttpResponse (" This is the task list")
