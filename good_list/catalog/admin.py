from django.contrib import admin
from django.contrib.auth.models import Group

from .models import HumanRecord
from .models import OrganizationRecord
from .models import NeedHelpPost
from .models import Respondent
from .models import NewsPost
from .models import ReportPost


# Конфигурация сайта админа
admin.site.site_header = 'Панель суперадмина'

admin.site.register(HumanRecord)
admin.site.register(OrganizationRecord)
admin.site.register(NeedHelpPost)
admin.site.register(Respondent)
admin.site.register(NewsPost)
admin.site.register(ReportPost)

admin.site.unregister(Group)

# Register your models here.
