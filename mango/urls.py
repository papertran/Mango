from django.urls import path
from django.conf.urls import url
from mango import views

app_name = 'mango'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('account/', views.account_view, name='account'),
    path('account/add_account/', views.add_account_view, name='add_account'),
    path('account/add_transaction/', views.add_transaction_view, name="add_transaction")
]