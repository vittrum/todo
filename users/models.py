from django.db import models


class Family(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'families'


class User(models.Model):
    name = models.CharField(max_length=50)
    earnings = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'users'
