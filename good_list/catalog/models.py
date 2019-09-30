from django.db import models
from django.urls import reverse


# Create your models here.

# Модель получающая записи для страницы "список добрых дел"
class GoodDeedRecord(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=500, null=True)
    # image = models.ImageField(null=True)

    # список выбора
    TYPES_OBJECT_FOR_HELP = (
        ('0', 'Частное лицо'),
        ('1', 'Организация')
    )
    typeHelpObj = models.CharField(max_length=20, choices=TYPES_OBJECT_FOR_HELP, default='1')

    adress = models.CharField(max_length=100, null=True)
    linkToWeb = models.CharField(max_length=100, null=True)
    phoneNumber = models.CharField(max_length=10, null=True)
    generalDescription = models.TextField(max_length=500, null=True)

    # список выбора
    STATUS_DISTURBANCES = (
        ('0', 'На рассмотрении'),
        ('1', 'Рассмотрено')
    )
    status = models.CharField(max_length=30, choices=STATUS_DISTURBANCES, default='1')

    creationDate = models.DateField()

    def __str__(self):
        return self.title
