from django.db import models

# Create your models here.
from users.models import User


class TodoTask(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=300)
    priority = models.CharField(max_length=10) # add choises
    goal_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "tasks"

    def __str__(self):
        return self.name

    