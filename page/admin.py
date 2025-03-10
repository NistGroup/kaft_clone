from django.contrib import admin
from .models import Page, Carousel

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        "pk",
        "title",
        "status",
        "updated_at",
    )

    list_filter = (
        "status",
    )

    list_editable = (
        "status",
        "title",
    )

class CarouselAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "title",
        "status",
        "updated_at",
    )

    list_filter = (
        "status",
    )

    list_editable = (
        "status",
        "title",
    )


    # def __str__(self):
    #     title = self.title


admin.site.register(Page, PageAdmin)
admin.site.register(Carousel)
