from django.contrib import admin
from .models import services, Category


# Customizing Services module in Admin Panel
class ServicesAdmin(admin.ModelAdmin):
    list_display = (
        'service',
        'category',
        'has_hours',
        'price',
        'active',
    )

    ordering = ('service',)


# Customizing Categories Module in Admin Panel
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'description',
        'active',
    )

    ordering = ('category',)


# Registering Category and Service Modules in Admin panel"

admin.site.register(services, ServicesAdmin)
admin.site.register(Category, CategoryAdmin)
