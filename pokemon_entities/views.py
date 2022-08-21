import folium

from django.shortcuts import render
from django.utils.timezone import localtime

from pokemon_entities.models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    now = localtime()
    pokemon_entities = PokemonEntity.objects.filter(
        appeared_at__lte=now,
        disappeared_at__gte=now
    )
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(pokemon_entity.pokemon.image.url)
        )

    pokemons = Pokemon.objects.all()
    pokemons_on_page = []
    for pokemon in pokemons:
        if pokemon.image:
            image_url = request.build_absolute_uri(pokemon.image.url)
        else:
            image_url = ''

        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': image_url,
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    pokemon_img_url = request.build_absolute_uri(pokemon.image.url)

    if pokemon.parent_id is None:
        previous_evolution = None
    else:
        parent = Pokemon.objects.get(id=pokemon.parent_id)
        previous_evolution = {
            'title_ru': parent.title,
            'pokemon_id': parent.id,
            'img_url': request.build_absolute_uri(parent.image.url),
        }

    child = pokemon.next_evolutions.first()
    if child is None:
        next_evolution = None
    else:
        next_evolution = {
            'title_ru': child.title,
            'pokemon_id': child.id,
            'img_url': request.build_absolute_uri(child.image.url),
        }

    serialized_pokemon = {
        'title_ru': pokemon.title,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'description': pokemon.description,
        'img_url': pokemon_img_url,
        'previous_evolution': previous_evolution,
        'next_evolution': next_evolution,
    }

    now = localtime()
    pokemon_entities = pokemon.entities.filter(
        appeared_at__lte=now,
        disappeared_at__gte=now
    )

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            pokemon_img_url
        )
    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': serialized_pokemon
    })
