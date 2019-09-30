from django.db import models
from django.urls import reverse

# Create your models  here.

# Модель получающая записи для страницы "список добрых дел"
class GoodDeedRecord(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=500, null=True)
    #image = models.ImageField(null=True)
    typeHelpObj = models.CharField(max_length=50)
    adress = models.CharField(max_length=100, null=True)
    linkToWeb = models.CharField(max_length=100, null=True)
    phoneNumber = models.CharField(max_length=10, null=True)
    generalDescription = models.TextField(max_length=500, null=True)
    status = models.CharField(max_length=30, null=True)
    creationDate = models.DateField()

    def get_absolute_url(self):
        return reverse('good_deed', args=[str(self.id)])