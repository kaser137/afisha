from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from afisha import settings
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('places/<int:place_id>/', place_detail_view, name='place_details'),
    path('', index),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)