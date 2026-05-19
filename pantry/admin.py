from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Register)
admin.site.register(product)
admin.site.register(cart)
admin.site.register(wish_list)
admin.site.register(Order)
admin.site.register(PasswordReset)
admin.site.register(Mail)
admin.site.register(deliveryboy)
admin.site.register(orderitem)