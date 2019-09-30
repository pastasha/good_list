from .views import index, IWantHelpList, HelpMeList, IWantHelpPost, INeedHelpPost
from django.conf.urls import url
from django.urls import path

'''
    Маршрутизатор приложения перенаправляющий на необходимые страницы
'''

urlpatterns = [
    # своя функиция обработчик для view
    url(r'^$', index, name='index'),
    url(r'^i_want_help_list/$', IWantHelpList.as_view(), name = 'i_want_help'),
    url(r'^help_me_list/$', HelpMeList.as_view(), name = 'help_me'),
    url(r'^i_want_help_post/(?P<pk>\d+)$', IWantHelpList.as_view(), name = 'post'),
    url(r'^i_need_help_post/(?P<pk>\d+)$', HelpMeList.as_view(), name = 'post')
]

