import json
import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, Image
from requests.exceptions import MissingSchema


class Command(BaseCommand):
    help = 'For run type: python3 manage.py load_place <full path of json file with place>'

    def add_arguments(self, parser):
        parser.add_argument("place's_json_file_urls", nargs='+', type=str)

    def handle(self, *args, **options):
        for place_url in options["place's_json_file_urls"]:
            try:
                response = requests.get(f'{place_url}')
                response.raise_for_status()
                place_details = response.json()
            except MissingSchema:
                with open(place_url, 'r') as file:
                    place_details = json.load(file)
            title = place_details['title']
            description_short = place_details.get('description_short', '')
            description_long = place_details.get('description_long', '')
            lng = place_details['coordinates']['lng']
            lat = place_details['coordinates']['lat']
            imgs = place_details.get('imgs', [])
            place, created = Place.objects.get_or_create(
                title=title,
                lng=lng,
                lat=lat,
                defaults={
                    'description_short': description_short,
                    'description_long': description_long,
                },
            )
            if not created:
                return
            for img_url in imgs:
                response = requests.get(img_url)
                response.raise_for_status()
                Image.objects.create(place=place, img=ContentFile(response.content, name='image_name'))
