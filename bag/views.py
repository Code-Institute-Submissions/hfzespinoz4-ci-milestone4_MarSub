from django.shortcuts import render


# A view to render the shopping bag.
def view_bag(request):
    return render(request, 'bag/bag.html')
