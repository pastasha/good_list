from django.contrib import admin


from .models import HumanRecord, OrganizationRecord, NeedHelpPost, Respondent, ReportPost


# Конфигурация сайта админа
admin.site.site_header = 'Панель суперадмина'

admin.site.register(HumanRecord)
admin.site.register(OrganizationRecord)
admin.site.register(NeedHelpPost)
admin.site.register(Respondent)
#admin.site.register(NewsPost)
admin.site.register(ReportPost)

