from django.db import models


class LegalEntity(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    #photo = models.ImageField

    def __str__(self):
        return self.name


class Individual(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    #photo = models.ImageField

    def __str__(self):
        return self.name