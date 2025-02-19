import json
import random
from classPokemon import Pokemon
from classManagePokemons import managePokemon

class Combat():  
    def __init__(self, name_player):
        # super().__init__()
        self.name_player = name_player
        self.pokemon_player = self.pokemon_player()
        self.pokemon_random = self.pokemon_random()
        self.type_multiplier = {
    "steel": {"steel": 0.5, "dragon": 0.5, "fairy": 0.5, "ice": 0.5, "bug": 0.5, 
              "normal": 0.5, "grass": 0.5, "psychic": 0.5, "rock": 0.5, "flying": 0.5, 
              "poison": 0, "fighting": 2, "fire": 2, "ground": 2},

    "fighting": {"bug": 0.5, "rock": 0.5, "dark": 0.5, 
                 "fairy": 2, "psychic": 2, "flying": 2},

    "dragon": {"water": 0.5, "electric": 0.5, "fire": 0.5, "grass": 0.5, 
               "dragon": 2, "fairy": 2, "ice": 2},

    "water": {"steel": 0.5, "water": 0.5, "fire": 0.5, "ice": 0.5, 
              "electric": 2, "grass": 2},

    "electric": {"steel": 0.5, "electric": 0.5, "flying": 0.5, 
                 "ground": 2},

    "fairy": {"fighting": 0.5, "bug": 0.5, "dark": 0.5, 
              "dragon": 0, "steel": 2, "poison": 2},

    "fire": {"steel": 0.5, "fairy": 0.5, "fire": 0.5, "ice": 0.5, "bug": 0.5, "grass": 0.5, 
             "water": 2, "rock": 2, "ground": 2},

    "ice": {"ice": 0.5, 
            "steel": 2, "fighting": 2, "fire": 2, "rock": 2},

    "bug": {"fighting": 0.5, "grass": 0.5, "ground": 0.5, 
             "fire": 2, "rock": 2, "flying": 2},

    "normal": {"ghost": 0, 
               "fighting": 2},

    "grass": {"water": 0.5, "electric": 0.5, "grass": 0.5, "ground": 0.5, 
              "fire": 2, "ice": 2, "bug": 2, "poison": 2, "flying": 2},

    "poison": {"fighting": 0.5, "fairy": 0.5, "bug": 0.5, "grass": 0.5, "poison": 0.5, 
               "psychic": 2, "ground": 2},

    "psychic": {"fighting": 0.5, "psychic": 0.5, 
                "bug": 2, "ghost": 2, "dark": 2},

    "rock": {"fire": 0.5, "normal": 0.5, "poison": 0.5, "flying": 0.5, 
             "steel": 2, "fighting": 2, "water": 2, "grass": 2, "ground": 2},

    "ground": {"poison": 0.5, "rock": 0.5, 
               "electric": 0, "water": 2, "ice": 2, "grass": 2},

    "ghost": {"bug": 0.5, "poison": 0.5, 
              "fighting": 0, "normal": 0, 
              "ghost": 2, "dark": 2},

    "dark": {"ghost": 0.5, "dark": 0.5, 
             "psychic": 0, "fighting": 2, "fairy": 2, "bug": 2},

    "flying": {"fighting": 0.5, "bug": 0.5, "grass": 0.5, 
               "ground": 0, "electric": 2, "ice": 2, "rock": 2}
}


    def pokemon_random(self):
        """Calcule la moyenne des expériences de base des Pokémon disponibles et sélectionne un Pokémon au hasard selon le range."""
        # 1. Calcul de la moyenne de l'expérience de base des Pokémon disponibles
        fighting_pokemons = managePokemon(self.name_player).fighting_pokemons()
        medium_level = sum(p.get_level() for p in fighting_pokemons) / len(fighting_pokemons)

        # 2. Vérification du range de la moyenne
        if 1 <= medium_level <= 91:
            experience_range = (1, 91)
        elif 91 < medium_level <= 201:
            experience_range = (91, 201)
        elif 201 < medium_level <= 351:
            experience_range = (201, 351)

        # 3. Charger les Pokémon du fichier pokédex.json qui ont une base_experience dans la plage
        with open('pokédex.json', 'r') as f:
                data = json.load(f)
                pokedex_data = data.get("pokemon", [])
        filtered_pokemons = [
            pokemon for pokemon in pokedex_data
            if experience_range[0] <= pokemon.get('base_experience', 0) <= experience_range[1]
        ]

        # comparer avec self.pokemon_list pour supprimer les pokemoons deja rencontrer de filtered_pokemons

        # 5. Sélectionner un Pokémon au hasard
        random_pokemon_data = random.choice(filtered_pokemons)
        random_pokemon = Pokemon(random_pokemon_data['name'])  # Crée un objet Pokémon à partir des données du fichier

        return random_pokemon


    def pokemon_player(self, ):
        pass # choisir entre les trois pékemon avalable

    def attacks_first(self):
        if self.pokemon_player.get_speed() > self.pokemon_random.get_speed():
            return self.pokemon_player, self.pokemon_random
        return self.pokemon_random, self.pokemon_player


    def calculate_damage(self, attacker, defender):  
        final_multiplier = 1
        for attacker_type in attacker.get_types():
            multiplier = 1
            for defender_type in defender.get_types():
                if defender_type in self.type_multiplier.get(attacker_type, {}):
                    multiplier *= self.type_multiplier[attacker_type][defender_type]

            if final_multiplier < multiplier:
                final_multiplier = multiplier

        damage = max(0, (attacker.get_attack() * final_multiplier) - defender.get_defense())
        return damage
    
    def perform_attack(self, attacker, defender):
        damage = self.calculate_damage(attacker, defender)
        defender.take_damage(damage)

        
    def battle(self):
        attacker, defender = self.attacks_first()
        while self.pokemon_player.is_alive() and self.pokemon_random.is_alive():
            self.perform_attack(attacker, defender)
            if not defender.is_alive():
                break
            self.perform_attack(defender, attacker)
        winner = self.pokemon_player if self.pokemon_player.is_alive() else self.pokemon_random
        if winner == self.pokemon_player:
            winner.level_up()
            winner.evolve()
            managePokemon(self.name_player).add_pokemon(self.pokemon_random)
            
    

    


        
