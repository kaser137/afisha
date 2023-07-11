from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from places.models import Place, Image

# admin.site.register(Place)
admin.site.register(Image)


class ImageInline(admin.TabularInline):
    model = Image
    raw_id_fields = ('place',)
    extra = 1

    def preview(self, obj):
        return format_html('<img src="{}" style="max-height: {}px;" />',
                           obj.img.url,
                           200,
                           )

    readonly_fields = ['preview']
    fields = (('order', 'img'), 'preview')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']
    inlines = [ImageInline, ]
    search_fields = ['title',]
    fields = (('title', 'lng', 'lat'), 'description_short', 'description_long')
