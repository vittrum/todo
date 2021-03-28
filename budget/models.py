from django.db import models

# Create your models here.


class Budget(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=300, null=True, blank=True)
    role = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=8)

    class Meta:
        db_table = 'budgets'

    def __str__(self):
        return self.name