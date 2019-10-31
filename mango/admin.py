from django.contrib import admin
from mango.models import userAccount, Account, Transactions
# Register your models here.

# This diplays the fields on the admin page
class adminFields(admin.ModelAdmin):
    list_display = ('email', 'username', 'userUUID', 'password', 'first_name', 'last_name')


admin.site.register(userAccount, adminFields)
admin.site.register(Account)
admin.site.register(Transactions)