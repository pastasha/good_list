from django.contrib import admin
from django.urls import include
from django.urls import path


'''
    Глобальный маршрутизатор проекта
'''

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('good_api/',include('good_api.urls')),
=======
# глобальный маршрутизатор перенаправит на локальный маршрутизатор приложения
    # список каталогов помощи
    path('catalog/',include('catalog.urls')),
    # главная страница
    path('', include('catalog.urls')),
    #path('',RedirectView.as_view(url='/catalog/', permanent=True)),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    #path('catalog/', include('catalog.urls')),
>>>>>>> dev
]

