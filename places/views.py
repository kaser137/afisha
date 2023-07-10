from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    payload = {"places": {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [37.62, 55.793676]
                },
                "properties": dict(title="«Легенды Москвы", placeId="moscow_legends",
                                   detailsUrl="static/moscow_legends.json")
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [37.64, 55.753676]
                },
                "properties": {
                    "title": "Крыши24.рф",
                    "placeId": "roofs24",
                    "detailsUrl": "static/roofs24.json"
                }
            }
        ]
    }}

    return render(request, 'places/index.html', context=payload)
