from django.db import models


class Place(models.Model):
    title = models.CharField(verbose_name='Название места', max_length=300)
    description_short = models.TextField(verbose_name='Краткое описание', max_length=300)
    description_long = models.TextField(verbose_name='Полное описание')
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, verbose_name='Место', related_name='images', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(verbose_name='позиция', default=0, db_index=True)
    img = models.ImageField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order} {self.place.title}'
