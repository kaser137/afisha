from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from places.models import Place


def index(request):
    places = Place.objects.all()
    features = []
    for place in places:
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('place_details', args=[place.id])
            }
        }
        features.append(feature)
    payload = {"places": {
        "type": "FeatureCollection",
        "features": features
    }
    }

    return render(request, 'places/index.html', context=payload)


def place_detail_view(reqest, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_details = dict(
        title=place.title,
        imgs=[image.img.url for image in place.images.all()],
        description_short=place.description_short,
        description_long=place.description_long,
        coordinates=dict(
            lng=place.lng,
            lat=place.lat,
        )
    )
    return JsonResponse(place_details, json_dumps_params={'ensure_ascii': False, 'indent': 4})
