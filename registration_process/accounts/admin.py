from django.contrib import admin
from .models import CustomUser, AdminUpdate

admin.site.register(CustomUser)
admin.site.register(AdminUpdate)
