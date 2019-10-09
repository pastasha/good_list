from django.contrib import admin
from django.contrib.auth.models import Group

<<<<<<< HEAD
# Register your models here.
=======
from .models import GoodDeedRecord

# Конфигурация сайта админа
admin.site.site_header = 'Панель суперадмина'

admin.site.register(GoodDeedRecord)
admin.site.unregister(Group)

# Register your models here.
>>>>>>> dev
