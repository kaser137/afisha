from django.contrib import admin

from places.models import Place, Image

# admin.site.register(Place)
admin.site.register(Image)


class ImageInline(admin.TabularInline):
    model = Image
    raw_id_fields = ('place',)
    extra = 1


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']
    inlines = [ ImageInline, ]



