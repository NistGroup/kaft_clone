from django.urls import path
from page.models import Carousel
from .views import (
    ### MANAGE ###
    manage_list,

    ### PAGE ###
    page_list,

    ### CAROUSEL ###
    carousel_create, 
    carousel_list, 
    carousel_update
)
urlpatterns = [

    ### CAROUSEL ###
    path('', manage_list, name='manage_list'), # Zaten ana urls.py da manage/ var
    path('carousel/list/', carousel_list, name='carousel_list'), 
    path('carousel/create/', carousel_create, name='carousel_create'), 
    path('carousel/update/<int:pk>/', carousel_update, name='carousel_update'), 


    ### PAGE ###
    path('page/list/',page_list , name='page_list'), 

]
