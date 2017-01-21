from django.db import models

# Create your models here.
class Task(models.Model):
    task_text = models.CharField(max_length=200)
    priority = models.IntegerField(default=0)
    assignee = models.ForeignKey(Person, on_delete=models.CASCADE)
    due_date = models.DateTimeField('date due')
    complete_data = models.DateTimeField('date complete')
