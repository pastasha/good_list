from .views import index
from django.conf.urls import url
from django.urls import path

'''
    Маршрутизатор приложения перенаправляющий на необходимые страницы
'''

urlpatterns = [
    # своя функиция обработчик для view
    path('', index)
]


'''
Этот подход вывода данных из БД не подходит

urlpatterns = [
    # Маршрутизатор вызывает шаблон который отобразится в браузере
    url('', BaseCatalogView.as_view(), name='catalog')
]
'''