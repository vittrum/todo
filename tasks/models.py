from django.db import models

# Create your models here.
from users.models import Member


class TodoTask(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=300)
    priority = models.CharField(max_length=10) # add choises
    assign_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "tasks"
        ordering = ['-assign_date']

    def __str__(self):
        return self.name