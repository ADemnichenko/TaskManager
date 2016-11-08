from django.conf.urls import url
from . import views
urlpatterns = [
   url(r'^$', views.task_list, name='task_list'),
   url(r'^delete/(?P<pk>[0-9]+)/$', views.task_del, name='task_del'),
   url(r'^complete/(?P<pk>[0-9]+)/$', views.task_complete, name='task_complete'),
   url(r'^start/(?P<pk>[0-9]+)/$', views.task_start, name='task_start'),
   url(r'^generator/$', views.auto_generator, name='auto_generator'),
]
