import uuid
from django.db import models

class Person(models.Model):
    """Person model for database.

    person_id: unique identifier for the person.
    person_text: text (name) of the person
    """
    person_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person_text = models.CharField(max_length=200)
    

class Task(models.Model):
    """Task model for the database.

    task_text: text (name) of the task to be completed.
    priority: integer representing priority of task (lower is high priority).
    assignee: Person assigned to the task.
    due_date: Date which the task needs to be completed by.
    complete_date: Date which the task was completed.
    """
    task_text = models.CharField(max_length=200)
    priority = models.IntegerField(default=0)
    assignee = models.ForeignKey(Person, on_delete=models.CASCADE)
    due_date = models.DateTimeField('date due')
    complete_date = models.DateTimeField('date complete')
