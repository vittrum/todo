from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    earnings = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'users'
