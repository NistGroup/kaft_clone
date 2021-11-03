from page.models import Carousel
import urllib

f = Carousel.objects.first()
print(f.title)

