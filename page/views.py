from django.shortcuts import render, redirect
from django.contrib import messages
from page.forms import CarouselModelForm
from .models import Carousel, Page

# Create your views here.


### USER ###
def index(request):
    context = dict()
    context['images'] = Carousel.objects.filter(
        status="published"
        ).exclude(cover_image = "")
    return render(request, "home/index.html", context)

def manage_list(request):
    context = dict()
    return render(request, "manage/manage.html", context)

def page_list(request):
    context = dict()
    context["items"] = Page.objects.all().order_by("-pk")
    return render(request, "manage/page_list.html", context)





### ADMİN ###
def carousel_list(request):
    context = dict()
    context["carousel"] = Carousel.objects.all().order_by("-pk")
    return render(request, "manage/carousel_list.html", context)

def carousel_update(request, pk):   # pk vermek zorundayız
    context = dict()
    # kaft_clone.com/manage/carousel/1/edit
    item = Carousel.objects.get(pk=pk)
    context['form'] = carousel_form(request, item)

    if request.method == "POST":
        form = CarouselModelForm(request.POST, request.FILES, instance=item)
        if form.is_valid:
            form.save()
            messages.success(request, "Veritabanı güncellendi.")
            return redirect("carousel_update", pk)

    return render(request, 'manage/carousel_form.html', context)


def carousel_create(request):
    context = dict()
    context['form'] = carousel_form()
    
    if request.method == 'POST':
        # print(request.POST)
        # print(request.FILES.get('cover_image'))
        # create code is deleted
        form = CarouselModelForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
        messages.success(request, 'Birseyler eklendi ama ne oldu bilemiyorum')
    return render(request, 'manage/carousel_form.html', context) 


def carousel_form(request=None, instance=None):
    if request:
        form = CarouselModelForm(
            request.POST, 
            request.FILES, 
            instance=instance,
        )
    else:
        form = CarouselModelForm(instance=instance)
    return form
