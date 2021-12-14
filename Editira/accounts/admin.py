from django.contrib import admin
from .models import Staff , Client , Offer , notification


# Register your models here.
admin.site.register(Staff)
admin.site.register(Client)
admin.site.register(Offer)
admin.site.register(notification)
