from django.shortcuts import render
from .models import Artist

# Create your views here.

def artist_detail(request, pk):
    
    artist = Artist.objects.get(pk=pk)
    return render(request, 'artists/artist_detail.html', {'artist': artist})