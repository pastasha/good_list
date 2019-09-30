from .views import index
from django.conf.urls import url
from django.urls import path

'''
    Маршрутизатор приложения перенаправляющий на необходимые страницы
'''

urlpatterns = [
<<<<<<< HEAD
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

    url(r'^$', views.index, name='index'),
    url(r'^i_want_help_list/$', views.IWantHelpList.as_view(), name = 'i_want_help'),
    url(r'^help_me_list/$', views.HelpMeList.as_view(), name = 'help_me'),
    url(r'^i_want_help_post/(?P<pk>\d+)$', views.IWantHelpList.as_view(), name = 'post'),
    url(r'^i_need_help_post/(?P<pk>\d+)$', views.HelpMeList.as_view(), name = 'post'),

]

>>>>>>> dev
