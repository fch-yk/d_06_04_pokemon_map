from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name='имя')
    image = models.ImageField(
        upload_to='images',
        blank=True,
        null=True,
        verbose_name='изображение'
    )
    description = models.TextField(default='', verbose_name='описание')
    title_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='имя (англ.)'
    )
    title_jp = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='имя (японск.)'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='next_evolutions',
        verbose_name='эволюционирует из'
    )

    def __str__(self) -> str:
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        verbose_name='покемон'
    )
    lat = models.FloatField(verbose_name='широта')
    lon = models.FloatField(verbose_name='долгота')
    appeared_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='появляется в'
    )
    disappeared_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='исчезает в'
    )
    level = models.IntegerField(blank=True, null=True, verbose_name='уровень')
    health = models.IntegerField(blank=True, null=True, verbose_name='здровье')
    strength = models.IntegerField(blank=True, null=True, verbose_name='сила')
    defence = models.IntegerField(blank=True, null=True, verbose_name='защита')
    stamina = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='выносливость'
    )

    def __str__(self) -> str:
        return f'{self.id}: location of {self.pokemon.title}'
