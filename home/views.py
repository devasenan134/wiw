from django.shortcuts import render
from .models import Video

# Create your views here.

def home(request):
    videos = Video.objects.all()

    return render(request, "home/home.html", {
        "videos": videos
    })

def blog(request):
    pass