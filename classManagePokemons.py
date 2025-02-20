import json
import os
from classPokemon import Pokemon

class managePokemon():
    def __init__(self, player_name):
        self.player_name = player_name
        self.file_path = f"{player_name}_pokeball.json"
        self.pokemon_list = self.load_pokemon()

    def load_pokemon(self):
        """Charge les Pokémon à partir du fichier JSON ou crée une équipe par défaut."""
        if not os.path.exists(self.file_path):
            self.create_default_team()

        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                if "pokeball" in data and isinstance(data["pokeball"], list):
                    return [Pokemon(pokemon["name"]) for pokemon in data["pokeball"]]  # Charge les Pokémon
        except (FileNotFoundError, json.JSONDecodeError):
            pass  # En cas d'erreur, on utilisera l'équipe par défaut

        self.create_default_team()  # Si on arrive ici, c'est qu'il y a eu un problème
        return self.pokemon_list

    def create_default_team(self):
        """Crée une équipe de Pokémon par défaut et sauvegarde dans un fichier."""
        self.pokemon_list = [
            Pokemon("pikachu"),
            Pokemon("bulbasaur"),
            Pokemon("squirtle")
        ]

        for p in self.pokemon_list:
            p.set_available()  # Active les Pokémon par défaut

        self.save_pokemon()

    def save_pokemon(self):
        """Sauvegarde la liste des Pokémon dans le fichier JSON."""
        try:
            with open(self.file_path, "w") as f:
                json.dump({"pokeball": [p.stats_pokemon_to_dict() for p in self.pokemon_list]}, f, indent=4)
        except IOError:
            print(f"Erreur : Impossible d'écrire dans le fichier {self.file_path}.")

    def remove_pokemon(self, pokemon_name):
        """Retire un Pokémon de l'équipe par son nom."""
        new_list = [p for p in self.pokemon_list if p.get_name() != pokemon_name]

        if len(new_list) < len(self.pokemon_list):
            self.pokemon_list = new_list
            self.save_pokemon()
            print(f"{pokemon_name} a été retiré de l'équipe.")
        else:
            print(f"Erreur : {pokemon_name} n'a pas été trouvé dans l'équipe.")

    def add_pokemon(self, new_pokemon):
        """Ajoute un Pokémon à l'équipe et met à jour le fichier JSON."""
        if any(p.get_name() == new_pokemon.get_name() for p in self.pokemon_list):
            print(f"Erreur : {new_pokemon.get_name()} est déjà dans l'équipe.")
        else:
            self.pokemon_list.append(new_pokemon)
            self.save_pokemon()

    def update_pokemon(self, updated_pokemon):
        """Met à jour un Pokémon s'il existe dans l'équipe."""
        for i, p in enumerate(self.pokemon_list):
            if p.get_id() == updated_pokemon.get_id():
                self.pokemon_list[i] = updated_pokemon
        self.save_pokemon()

    def list_pokemon(self):
        """Retourne une liste des noms des Pokémon dans l'équipe."""
        return [p.get_name() for p in self.pokemon_list]

    def update_availability(self, pokemon_name, available):
        """Met à jour la disponibilité d'un Pokémon."""
        available_count = sum(1 for p in self.pokemon_list if p.get_available())

        for p in self.pokemon_list:
            if p.get_name() == pokemon_name:
                if available:
                    if available_count < 3 and not p.get_available():
                        p.set_available()
                        self.save_pokemon()
                    elif available_count >= 3:
                        print("Erreur : Il y a déjà 3 Pokémon disponibles. Impossible d'en activer un autre.")
                else:
                    if p.get_available():
                        p.set_available()  # Désactive le Pokémon
                        self.save_pokemon()
                return

    def fighting_pokemons(self):
        """Retourne une liste des Pokémon disponibles pour le combat."""
        with open(self.file_path, 'r') as f:
            data = json.load(f)

        available_pokemon = [pokemon["name"] for pokemon in data.get("pokeball", []) if pokemon.get("available", True)]
        
        return available_pokemon
