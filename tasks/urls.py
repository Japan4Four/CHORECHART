from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # Make the regex below match /task_list/
    url(r'^task_list$', views.task_list, name='task_list')
    # Broken list
]
