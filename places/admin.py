from django.contrib import admin

from places.models import Place, Image

# admin.site.register(Place)
admin.site.register(Image)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']
