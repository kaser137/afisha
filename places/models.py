from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(verbose_name='Название места', max_length=300)
    description_short = models.TextField(verbose_name='Краткое описание', blank=True)
    description_long = HTMLField(verbose_name='Полное описание', blank=True)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    class Meta:
        unique_together = [['title', 'lng', 'lat']]

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, verbose_name='Место', related_name='images', on_delete=models.CASCADE, null=True)
    order = models.PositiveIntegerField(verbose_name='позиция', default=0, db_index=True)
    img = models.ImageField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.img.name
