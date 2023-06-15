from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('applyjob',views.applyjob,name='applyjob'),
    path('searchjob',views.searchjob,name='searchjob'),
]
