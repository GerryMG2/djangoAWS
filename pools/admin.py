from django.contrib import admin
from .models import Categories,Customers,Employees,Orderdetails,Orders,Products,Shippers,Suppliers

# Register your models here.

admin.site.register(Categories)
admin.site.register(Customers)
admin.site.register(Employees)
admin.site.register(Orderdetails)
admin.site.register(Orders)
admin.site.register(Products)
admin.site.register(Shippers)
admin.site.register(Suppliers)

