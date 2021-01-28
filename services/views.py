from django.shortcuts import render, get_object_or_404
from .models import Services


# A view to render the services page.
def all_services(request):
    services = Services.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'services/services.html', context)


# A view to render service details page
def service_details(request, service_id):
    service = get_object_or_404(Services, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'services/services_details.html', context)
