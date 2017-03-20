from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^add/$', views.add_task, name='add_task'),
    url(r'^del/(?P<pk>\d+)$', views.task_delete, name='task_delete'),
    url(r'^del-card/(?P<pk>\d+)', views.task_card_delete, name='task_card_delete'),
    url(r'^add-list/', views.task_add_list, name='task_add_list'),
    url(r'^feedback/$', views.feedback, name='feedback'),

]