from django.contrib.auth import get_user_model
from django.db import models
User=get_user_model()

# Create your models here.
class Todo(models.Model):
    NEW='new'
    FINISHED='finished'
    STATUS=[
        (NEW,'new'),
        (FINISHED,'finished'),
    ]
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    status=models.CharField(choices=STATUS, max_length=20, default=NEW)
    title=models.CharField(max_length=120)
    description=models.CharField(max_length=512)
    def mark_as_finished(self):
        self.status=self.FINISHED
        self.save()
    def mark_as_unfinfished(self):
        self.status=self.NEW
        self.save()



