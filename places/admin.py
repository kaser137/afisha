from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.StackedInline):
    model = Image
    raw_id_fields = ('place',)
    extra = 0

    @staticmethod
    def preview(image: Image):
        return format_html(
            '<img src="{}" style="max-height: {}px;" />',
            image.img.url,
            200
        )

    readonly_fields = ['preview']
    fields = ('order', 'img', 'preview')


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ['title', 'id']
    inlines = [ImageInline, ]
    search_fields = ['title', ]
    fields = (('title', 'lng', 'lat'), 'description_short', 'description_long')
    ordering = ['id']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
