from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html')

def contact(request):
    """ A view to return the about us page """
    
    return render(request, 'home/contact_us.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response