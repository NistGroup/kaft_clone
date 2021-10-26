
from django.contrib import admin
from django.urls import path, include
from page.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', index, name="index"),
  path('manage/', include("page.urls"),),
  path('admin/', admin.site.urls),
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

