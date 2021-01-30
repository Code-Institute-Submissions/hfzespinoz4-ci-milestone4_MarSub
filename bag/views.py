from django.shortcuts import (
    render, redirect, reverse,  get_object_or_404, HttpResponse)
from services.models import Services
from django.contrib import messages


# A view to render the shopping bag.
def view_bag(request):
    return render(request, 'bag/bag.html')


# The Add to bag view_bag.
def add_to_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    service = get_object_or_404(Services, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, (f'Updated {service.service} ' f'quantity to {bag[item_id]}'))
    else:
        bag.pop(item_id)
        messages.success(request, (f'Removed {service.service} ' f'from your bag'))

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        service = get_object_or_404(Services, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed {service.service} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
