import json
from random import randint

def add_player():
    """
    createsa json file with name of new player
    and his/her 3 pokemons
    """
    print("Bonjour nouveau dresseru, quel est ton nom ?")
    name_player = input()
    list_of_pokemons = creates_pokemon_list()

    # créér 1 fichier json avec le nom du joueur et ses 3 pokemons de départ
    new_player = name_player, list_of_pokemons

    try :
        with open("./new_player.json", "w") as file:
            json.dump(new_player, file)

    except ( IOError, OverflowError) as error :
        print("Error while writing")
    except (IsADirectoryError, FileNotFoundError, NameError, OSError, PermissionError) as error :
            print("Error with file or OS error")
    except (UnicodeDecodeError, UnicodeEncodeError) as error :
        print("Error with encoding or decoding")
    except Exception :
        print("Error while writing")


def creates_pokemon_list():
    """
    creates then return
    a list of 3 different pokemons
    """

    with open("pokeessai.json", "r") as f :
        list_poke = json.load(f)

    # transformer le json en une liste
    indices_poke = [poke for poke in list_poke]
    print(type(list_poke))

    indice = randint(0, len(list_poke)-1)

    indexes_pokemons = set()
    while len(indexes_pokemons) < 3 :
        indice = randint(0, len(list_poke)-1)
        indexes_pokemons.add(indice)

    list_pokemons = [indices_poke[i] for i in indexes_pokemons]
    print(list_pokemons)
    return list_pokemons