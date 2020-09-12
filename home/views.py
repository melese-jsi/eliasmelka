from django.shortcuts import render,get_object_or_404
from .models import Music, Interview


# Create your views here.
def home(request):
    albums = Music.objects.all()
    return render(request,'home/home.html',{'albums':albums})

def album_detail(request,album_id):
    album = get_object_or_404(Music,pk=album_id)
    return render(request, 'home/album_detail.html',{'album':album})

def recent_releases(request):
    albums = Music.objects.filter(release_year__gte = 2008)
    albums = albums.order_by('release_year')
    return render(request, 'home/recent_releases.html', {'albums': albums})

def popular_albums(request):
    albums = Music.objects.filter(is_popular__exact = True)
    return render(request, 'home/popular_albums.html', {'albums': albums})
def community_songs(request):
    albums = Music.objects.filter(is_community_song__exact=True)
    return render(request, 'home/community_songs.html', {'albums': albums})
def all_albums(request):
    albums = Music.objects.filter(is_album__exact=True)
    return render(request, 'home/home.html', {'albums': albums})

def interviews(request):
    interviews = Interview.objects.all()
    return render(request,'home/interviews.html',{'interviews':interviews})