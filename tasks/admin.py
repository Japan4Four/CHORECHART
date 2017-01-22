from django.contrib import admin

from .models import Task, Person

admin.site.register(Task)
admin.site.register(Person)
