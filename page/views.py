from django.shortcuts import render
from django.contrib import messages
from .models import Carousel

# Create your views here.

def index(request):
    context = dict()
    context['images'] = Carousel.objects.filter(status="published")
    return render(request, "home/index.html", context)

def carousel_create(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES["cover_image"])
        messages.success(request, "Birşeyler eklendi ama ne oldu bilemiyorum")
    return render(request, "manage/carousel_create.html", {})