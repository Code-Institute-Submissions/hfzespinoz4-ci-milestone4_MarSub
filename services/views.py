from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Services, Category
from .forms import ServiceForm


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


@login_required
def add_service(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save()
            messages.success(request, 'Successfully added!')
            return redirect(reverse('product_detail', args=[service.id]))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ServiceForm()

    template = 'service/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_service(request, service_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    service = get_object_or_404(Services, pk=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated service!')
            return redirect(reverse('service_detail', args=[service.id]))
        else:
            messages.error(request,
                           ('Failed to update product. '
                            'Please ensure the form is valid.'))
    else:
        form = ServiceForm(instance=service)
        messages.info(request, f'You are editing {service.service}')

    template = 'services/edit_services.html'
    context = {
        'form': form,
        'service': service,
    }

    return render(request, template, context)


@login_required
def delete_service(request, service_id):
    """ Delete a service  """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    service = get_object_or_404(Services, pk=service_id)
    service.delete()
    messages.success(request, 'Service deleted!')
    return redirect(reverse('products'))
