from django.contrib import admin
from .models import services, Category

# Registering Category and Service Modules in Admin panel"
admin.site.register(services)
admin.site.register(Category)
