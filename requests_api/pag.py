import requests
def get_all_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon"
    
    list_pokemons = []
    while url:
        response = requests.get(url)
        data = response.json()
        list_pokemons.extend(data['results'])
        url = data['next']
    return list_pokemons

pokemon = get_all_pokemon()
print('Total pokemon:', pokemon)
print('Total:', len(pokemon))




