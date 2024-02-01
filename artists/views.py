from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the artist detail page """
    
    return render(request, 'artists/artist_detail.html')