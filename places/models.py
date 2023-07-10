from django.db import models


class Place(models.Model):
    title = models.CharField(verbose_name='Название места', max_length=300)
    description_short = models.CharField(verbose_name='Краткое описание', max_length=300)
    description_long = models.TextField(verbose_name='Полное описание')
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title