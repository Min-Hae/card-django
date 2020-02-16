from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=30)
    bank = models.CharField(max_length=20)
    af = models.CharField(max_length=10)
    benefit = models.TextField()
    bn = models.CharField(max_length=15)

    class Meta:
        ordering = ['bank', 'name']

    def __str__(self):
        return self.name