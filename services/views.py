from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Services


# A view to render the services page.
def all_services(request):
    services = Services.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search criteria")
                return redirect(reverse('services'))

            queries = Q(service__icontains=query) | Q(description__icontains=query)
            services = services.filter(queries)

    context = {
        'services': services,
        'search_term': query,
    }

    return render(request, 'services/services.html', context)


# A view to render service details page
def service_details(request, service_id):
    service = get_object_or_404(Services, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'services/services_details.html', context)
