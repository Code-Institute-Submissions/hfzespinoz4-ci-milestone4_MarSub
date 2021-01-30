from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

# Update order total on lineitem update/create
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs)
    instance.order.update_total()


# Update order total on lineitem update/delete
@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs)
    instance.order.update_total()
