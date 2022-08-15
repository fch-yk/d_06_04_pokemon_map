from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self) -> str:
        return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)
