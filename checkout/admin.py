from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInLine(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInLine,)
    readonly_fields = ('order_number', 'date', 'order_total',)

    fields = ('full_name', 'email', 'phone_number',
              'country', 'postcode', 'town_or_city',
              'street_address1', 'street_address2',
              'county', 'date', 'order_total',
              'order_progress', 'order_status',)

    list_display = ('order_number', 'full_name', 'date',
                    'order_total', 'order_progress', 'order_status',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
