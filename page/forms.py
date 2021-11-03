from django import forms
from django.forms import fields
from .models import Carousel

class CarouselModelForm(forms.ModelForm):
    class Meta:
        model = Carousel
        fields = "__all__"
