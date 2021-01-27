from django.shortcuts import render
from .models import Services


# Create your views here.
def all_services(request):
    """ A view to render the services page """

    services = Services.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'services/services.html', context)
