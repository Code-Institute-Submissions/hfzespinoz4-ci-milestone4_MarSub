from django.shortcuts import get_object_or_404
from services.models import Services


# Dictionary with bag items
def bag_contents(request):
    bag_items = []
    total = 0
    service_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        service = get_object_or_404(Services, pk=item_id)
        total += quantity * service.price
        service_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'service': service,
        })

    grand_total =  total

    context = {
        'bag_items': bag_items,
        'total': total,
        'service_count': service_count,
    }

    return context
