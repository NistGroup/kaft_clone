from django.shortcuts import render
from .models import Carousel

# Create your views here.

def index(request):
    context = dict()
    context['images'] = Carousel.objects.filter(status="published")
    return render(request, "home/index.html", context)