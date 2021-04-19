from django.db import models

# Create your models here.
from users.models import Family


class Budget(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=300, null=True, blank=True)
    date_from = models.DateField()
    date_to = models.DateField()
    participant = models.ForeignKey(Family, on_delete=models.CASCADE)

    class Meta:
        db_table = 'budgets'

    def __str__(self):
        return self.name
