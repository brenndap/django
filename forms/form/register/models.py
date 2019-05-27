from django.db import models

# Create your models here.


class Subscription(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    made_in = models.DateTimeField('made in', auto_now_add=True)

    # class Meta:
    #     ordering = ['made_in']
    #     verbose_name = u'name'
    #     verbose_name_plural = u'names'

    def __unicode__(self):
        return self.name

