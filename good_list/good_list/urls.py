from django.contrib import admin
from django.urls import include
from django.urls import path


'''
    Глобальный маршрутизатор проекта
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    # список каталогов помощи
    #path('catalog/',include('catalog.urls')),
    # главная страница
    path('', include('good_api.urls')),
    path('good_api/', include('good_api.urls')),
]

