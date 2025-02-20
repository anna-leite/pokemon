import json
import  random

class Pokemon:
    def __init__(self, name):
        self.__name = name
        self.__id = self.get_pokemon_info(name, "id")
        self.__types = self.get_pokemon_info(name, "types") 
        self.__evolution = self.get_pokemon_info(name, "evolution")  
        self.__level = random.randint(5, 20) 
        self.__hp = self.get_pokemon_info(name, "hp")  
        self.__attack = self.get_pokemon_info(name, "attack") 
        self.__defense = self.get_pokemon_info(name, "defense") 
        self.__speed = self.get_pokemon_info(name, "speed") 
        self.__available = False


    def __str__(self):
        return f"{self.__name} (Types : {', '.join(self.__types)}, HP: {self.__hp}, Level: {self.__level}, Attack: {self.__attack}, Defense: {self.__defense}, Speed: {self.__speed}, Evolution: {self.__evolution})"

    def is_alive(self):
        return self.__hp > 0 # boléen
    
    def take_damage(self, damage):
        self.__hp -= damage
        if self.__hp < 0:
            self.__hp = 0
          
    def level_up(self):
        gain_level =  random.randint(1, 3)
        self.__level += gain_level
        self.__attack += random.randint(0, 3) +  gain_level  # Augmente de manière aléatoire
        self.__defense += random.randint(0, 3) + gain_level  
        self.__hp += random.randint(0, 3) + gain_level 
        self.__speed = random.randint(0, 3) + gain_level 


    def evolve(self):
        if self.__level >= self.get_pokemon_info(self.__name, "base_experience"):
            if self.__evolution:
                self.__name = self.__evolution
                self.__types = self.get_pokemon_info(self.__name, "types")
                self.__evolution = self.get_pokemon_info(self.__name,"evolution")
                self.__attack = self.get_pokemon_info(self.__name,"attack")
                self.__defense = self.get_pokemon_info(self.__name,"defense")
                self.__hp = self.get_pokemon_info(self.__name,"hp")
                self.__speed = self.get_pokemon_info(self.__name,"speed")
            else: 
                print(f"{self.__name} ne peut pas évoluer davantage.")


    def get_pokemon_info(self, name, info):
        try:
            with open('pokedex.json', 'r') as f :
                data = json.load(f)
                pokemon_data = data.get("pokemon", [])

                for pokemon in pokemon_data:
                    if pokemon['name'].lower() == name.lower():
                        return pokemon.get(info, None)
        except FileNotFoundError:
            print("pokedex.json non trouvé.")
        except json.JSONDecodeError:
            print("Erreur lors du chargement du fichier JSON")

        print("Le Pokémon n'existe pas.")

    def stats_pokemon_to_dict(self,):
        return {
            "name": self.__name,
            "types": self.__types,
            "level": self.__level,
            "hp": self.__hp,
            "attack": self.__attack,
            "defense": self.__defense,
            "speed": self.__speed,
            "evolution": self.__evolution,
            "available": self.__available
        }
    

    def set_available(self):
        self.__available = not self.__available


    # Getters :
    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def get_types(self):
        return self.__types
    
    def get_level(self):
        return self.__level
    
    def get_hp(self):
        return self.__hp
    
    def get_speed(self):
        return self.__speed
    
    def get_attack(self):
        return self.__attack
    
    def get_defense(self):
        return self.__defense
    
    def get_evolution(self):
        return self.__evolution

    def get_available(self):
        return self.__available
    


    

    

