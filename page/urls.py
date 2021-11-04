from django.urls import path
from page.models import Carousel
from .views import carousel_create, carousel_list

urlpatterns = [
    path('carousel_create/', carousel_create, name="carousel_name"),
    path('carousel_list/', carousel_list, name="carousel_title"),
]
