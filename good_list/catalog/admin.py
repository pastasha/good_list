from django.contrib import admin

# Register your models here.
from .models import GoodDeedRecord

admin.site.register(GoodDeedRecord)
#@admin.register(GoodDeedRecord)
#class BookAdmin(admin.ModelAdmin):
#    list_display = ('title', 'description', 'typeHelpObj', 'adress', 'linkToWeb', 'phoneNumber', 'generalDescription', 'status', 'creationDate')
#    fields = ['title', 'description', 'typeHelpObj', 'adress', 'linkToWeb', 'phoneNumber', 'generalDescription', 'status', 'creationDate']
