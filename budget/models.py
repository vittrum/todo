from django.db import models

from users.models import Member


class Budget(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    summ = models.IntegerField()
    date_granted = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'budgets'

    def __str__(self):
        return self.name
