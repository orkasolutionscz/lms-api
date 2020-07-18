from django.contrib import admin
from api_customer.models import Customers
#
#
# class CustomersAdmin(BaseUserAdmin):
#     ordering = ['id']
#     list_display = ['email', 'name']
#
#
admin.site.register(Customers)
