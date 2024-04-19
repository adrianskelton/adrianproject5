from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def contact(request):
    """ A view to return the about us page """

    return render(request, 'home/contact_us.html')


    # Function that will be called when a 404 error occurs
def custom_404(request, exception):
    """
    Custom 404 error view.
    """
    return render(request, '404.html', status=404)

# Function that will be called when a 404 error occurs
def custom_400(request):
    """
    Custom 400 error view.
    """
    return render(request, '400.html', status=404)

# Function that will be called when a 500 error occurs
def custom_500(request):
    """
    Custom 500 error view.
    """
    return render(request, '500.html', status=500)