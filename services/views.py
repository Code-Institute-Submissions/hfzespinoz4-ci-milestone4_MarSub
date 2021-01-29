from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Services, Category


# A view to render the services page.
def all_services(request):
    services = Services.objects.all()
    query = None
    categories = None

    # Search functionallity,
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['Category'].split(',')
            services = services.filter(category__category__in=categories)
            categories = Category.objects.filter(category__in=categories)

        # Search field functionallity
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search criteria")
                return redirect(reverse('services'))

            # Filtering from Service and Categories Models
            queries = Q(service__icontains=query) | Q(description__icontains=query) | Q(short_description__icontains=query)
            services = services.filter(queries)

    context = {
        'services': services,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'services/services.html', context)


# A view to render service details page
def service_details(request, service_id):
    service = get_object_or_404(Services, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'services/services_details.html', context)
