from django.db import models

# Create your models here.
from users.models import Member


class Purchase(models.Model):
    name = models.CharField(max_length=50)
    info = models.CharField(max_length=300, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)

    class Meta:
        db_table = 'purchases'

    def __str__(self):
        return self.name
