from django.db import models

# Create your models here.


class Count(models.Model):

    counter = models.PositiveIntegerField(default=0)

