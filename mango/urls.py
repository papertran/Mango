from django.urls import path
from django.conf.urls import url
from mango import views

app_name = 'mango'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
]