from page.models import Carousel
import urllib

print(Carousel.objects.filter(status="published").count())
