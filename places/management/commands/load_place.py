import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, Image


class Command(BaseCommand):
    help = 'For run type: python3 manage.py load_place <full path of json file with place>'

    def add_arguments(self, parser):
        parser.add_argument("place's_json_file_urls", nargs='+', type=str)

    def handle(self, *args, **options):
        for place_url in options["place's_json_file_urls"]:
            response = requests.get(f'{place_url}')
            response.raise_for_status()
            place_details = response.json()
            title = place_details['title']
            description_short = place_details['description_short']
            description_long = place_details['description_long']
            lng = place_details['coordinates']['lng']
            lat = place_details['coordinates']['lat']
            imgs = place_details['imgs']
            obj, created = Place.objects.get_or_create(title=title, description_short=description_short,
                                                       description_long=description_long, lng=lng, lat=lat)
            if created:
                for img_url in imgs:
                    response = requests.get(img_url)
                    response.raise_for_status()
                    image = Image.objects.create(place=obj)
                    image.img.save('image_name', ContentFile(response.content), save=True)
