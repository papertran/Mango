from django.urls import path
from django.conf.urls import url
from mango import views
from .views import transactionUpdate, transactionsList, transactionDelete

app_name = 'mango'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('account/', views.account_view, name='account'),
    path('account/add_account/', views.add_account_view, name='add_account'),
    path('account/add_transaction/', views.add_transaction_view, name="add_transaction"),
    path('account/transactions_list', transactionsList.as_view(), name="transaction_list"),
    path('account/transactions_list/update_transaction/<int:pk>', transactionUpdate.as_view(), name="update_transaction"),
    path('account/transactions_list/delete_transaction/<int:pk>', transactionDelete.as_view(), name="delete_transaction"),

]