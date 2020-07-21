import requests
import json

# 1. Make a GET request to https://pokeapi.co/api/v2/pokemon?limit=151
#   This page has the first 151 pokemon
#   Take some time to explore the website
#   Think about how you can get the data
request = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
# 2. Make your response readable
request = request.json()
# 3. Create an empty list that you will put your data into
poke_info = {}
# 4. Loop through all of the 151 pokemon
pokemons = request["results"]
for pokemon in pokemons:
    # 5. Get the name of the pokemon
    name = pokemon['name']
    # 6. Get the link to the additional info
    url = pokemon['url']
    # 7. Make a GET request to the link

    info = requests.get(url)
    # 8. Make your response readable
    info = info.json()
    # 9. Get the ability of the pokemon
    #    Hint: If you are having trouble finding the
    #          ability, explore the data in your browser.
    #          Trial and error is your friend.
    abilities = info["abilities"]
    abilities_ = []
    for i in abilities:
        ability_ = i
        for j in ability_:
            if j == "ability":
                ability = ability_["ability"]
                ability = ability["name"]
                abilities_.append(ability)
    # 10. Append a dictionary to the list with the name
    #     and the ability of the pokemon
    poke_info[name] = abilities_
# 11. Loop through your list and print the name of the
#     pokemon and their ability
for i in poke_info:
    print(i, poke_info[i])
