from django.db import models

# Create your models here.


class Musician(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Musician, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):  # tabela intermediária
    person = models.ForeignKey(Musician, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invited_reason = models.CharField(max_length=100)


