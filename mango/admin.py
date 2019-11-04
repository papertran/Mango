from django.contrib import admin
from mango.models import userAccount, Account, Transactions
# Register your models here.

# This diplays the fields on the admin page
class adminFields(admin.ModelAdmin):
    list_display = ('email', 'username', 'userUUID', 'password', 'first_name', 'last_name')

class accountFields(admin.ModelAdmin):
    list_display = ('account_ID', 'account_PlaidID', 'account_name', 'account_type', 'user_id')

class transactionFields(admin.ModelAdmin):
    list_display = ('transaction_ID', 'transaction_plaidID', 'transaction_name', 'transaction_amount', 'transaction_date', 'transaction_location', 'account_ID', 'user_id')

admin.site.register(userAccount, adminFields)
admin.site.register(Account, accountFields)
admin.site.register(Transactions, transactionFields)