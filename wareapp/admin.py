from types import new_class
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(Customer)
admin.site.register(Inventory)
admin.site.register(Price)
admin.site.register(OrderItem)


# SuperUser
# Username: neal 
# Password: 1234 