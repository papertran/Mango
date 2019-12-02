from django.contrib import admin
from mango.models import userAccount, Account, Transactions, Category
# Register your models here.

# This diplays the fields on the admin page
class adminFields(admin.ModelAdmin):
    list_display = ('email', 'username', 'user_id', 'password', 'first_name', 'last_name')

class accountFields(admin.ModelAdmin):
    list_display = ('account_ID', 'account_PlaidID', 'account_name', 'account_type', 'user')

class transactionFields(admin.ModelAdmin):
    list_display = ('transaction_ID', 'transaction_plaidID', 'transaction_name', 'transaction_amount', 'transaction_date', 'transaction_location', 'account')

class categoryFields(admin.ModelAdmin):
    list_display = ('category_ID', 'category_name', 'category_color')
admin.site.register(userAccount, adminFields)
admin.site.register(Account, accountFields)
admin.site.register(Transactions, transactionFields)
admin.site.register(Category, categoryFields)