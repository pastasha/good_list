from .views import HomePageView
from django.conf.urls import url
from django.urls import path

'''
    Маршрутизатор приложения перенаправляющий на необходимые страницы
'''

urlpatterns = [
    # Маршрутизатор вызывает шаблон который отобразится в браузере
    path('', HomePageView.as_view(), name='home')
]

