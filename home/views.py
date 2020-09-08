from django.shortcuts import render,get_object_or_404
from .models import Music
# Create your views here.
def home(request):
    albums = Music.objects.all()
    return render(request,'home/home.html',{'albums':albums})

def album_detail(request,album_id):
    album = get_object_or_404(Music,pk=album_id)
    return render(request, 'home/album_detail.html',{'album':album})