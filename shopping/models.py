from django.db import models

# Create your models here.


class Purchase(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=300, blank=True, null=True)
    role = models.CharField(max_length=50, default='member')
    price = models.DecimalField(decimal_places=2, max_digits=8)

    class Meta:
        db_table = 'purchases'

    def __str__(self):
        return self.name
