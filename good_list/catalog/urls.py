from . import views
from django.conf.urls import url

'''
    Маршрутизатор перенаправляющий на необходимые страницы
'''

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^i_want_help_list/$', views.IWantHelpList.as_view(), name = 'i_want_help'),
    url(r'^help_me_list/$', views.HelpMeList.as_view(), name = 'help_me'),
    url(r'^i_want_help_post/(?P<pk>\d+)$', views.IWantHelpList.as_view(), name = 'post'),
    url(r'^i_need_help_post/(?P<pk>\d+)$', views.HelpMeList.as_view(), name = 'post'),

]

