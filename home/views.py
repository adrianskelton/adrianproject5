from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def contact(request):
    """ A view to return the about us page """

    return render(request, 'home/contact_us.html')


def custom_404(request, exception):
    return render(request, '404.html')

def custom_500(request):
    return render(request, '500.html')