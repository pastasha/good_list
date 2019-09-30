from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static #для добавления статических файлов


'''
    Глобальный маршрутизатор проекта
'''

urlpatterns = [
    path('admin/', admin.site.urls),
# глобальный маршрутизатор перенаправит на локальный маршрутизатор приложения
    # список каталогов помощи
    path('catalog/',include('catalog.urls')),
    # главная страница
    path('', include('catalog.urls')),
    #path('',RedirectView.as_view(url='/catalog/', permanent=True)),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    #path('catalog/', include('catalog.urls')),
]

