'''
Created on Sep 20, 2016

@author: Damilola
'''
from django.conf.urls import url
from . import views


urlpatterns =[
              
             url(r'^home/$', views.home, name='home_page'), 
              
]