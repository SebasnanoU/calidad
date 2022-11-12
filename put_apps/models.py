from django.db import models


class Galeria(models.Model):
    name = models.TextField(max_length=100)
    age = models.IntegerField()
    value = models.TextField()