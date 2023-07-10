from django.http import HttpResponse
from django.shortcuts import render

from places.models import Place


def index(request):
    places = Place.objects.all()
    features = []
    for place in places:
        feature = {
            'type': 'Feature',
            'geometry':{
                'type': 'Point',
                'coordinates': [place.lng, place.lat]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailUrl':''
            }
        }
        features.append(feature)
    payload = {"places": {
        "type": "FeatureCollection",
        "features": features
        }
    }

    return render(request, 'places/index.html', context=payload)
