import json
import  random

class Pokemon:
    def __init__(self, name):
        self.__name = name
        self.__type, self.__evolution = self.get_pokemon_info(name) # types et evolution sont récupéré à partir de json
        self.__level = random.randint(1, 10) # niveau aléatoire entre 1 et 10
        self.__hp = random.randint(1, 10) * self.__level # génère une attaque aléatoire basée sur le niveau
        self.__attack = random.randint(1, 10) * self.__level
        self.__defense = random.randint(1, 10) * self.__level
        self.__speed = max(1, 100 - self.__defence + random.randint(-5, 5)) # vitesse calculée en fonction de la défense, max() garantit que la valeur minimal de la vitesse est 1.


    def __str__(self):
        return f"{self.__name} (Types : {', '.join(self.__types)}, HP: {self.__hp}, Level: {self.__level}, Attack: {self.__attack}, Defense: {self.__defense}, Speed: {self.__speed}, Evolution: {self.__evolution})"

    def is_alive(self):
        return self.__hp > 0 # boléen
    
    def take_damage(self):
        pass
    
    def level_up(self):
        if self.__level < 100:
            gain_level =  random.randint(1, 3)
            self.__level += gain_level
            self.__attack += random.randint(1, 5) +  gain_level  # Augmente l'attaque de manière aléatoire
            self.__defense += random.randint(1, 5) + gain_level  # Augmente la défense de manière aléatoire
            self.__hp += random.randint(5, 10) + gain_level # Augmente les points de vie de manière aléatoire
            self.__speed = random.randint(1, 5) + gain_level # Augmante la vitesse de manière aléatoire
        #     print(f"{self.__name} a gagné un niveau! Nouveau niveau: {self.__level}")
        #     print(f"Nouvelles statistiques - Attack: {self.__attack}, Defense: {self.__defense}, HP: {self.__hp}, Speed: {self.__speed}")
        # else:
        #     print(f"{self.__name} a atteint le niveau maximum!")

    # rajouter une limite d'évolution dans le fichier json?
    # genre level_evolution = 30 et comparer le niveau automatiquement à chaque fin de match?
    def evolve(self):
        if self.__evolution:
            # print(f"{self.__name} évolue en {self.__evolution}!")
            evolved_pokemon = self.get-pokemon_info(self.__evolution)
            if evolved_pokemon:
                self.__name = self.__evolution
                self.__types, self.__evolution = evolved_pokemon
                self.__attack += random.randint(5, 15)
                self.__defense += random.randint(5, 15)
                self.hp += random.randint(10, 20)
                self.__speed = max(1, 100 - self.__defense + random.randint(-5, 5)) 
                # print(f"Nouvelles statistiques - Attack: {self.__attack}, Defense: {self.__defense}, HP: {self.__hp}, Speed: {self.__speed}")
            else:
                print(f"Erreur: {self.__evolution} non trouvé dans le fichier pokemon.json.")
        else: 
            print(f"{self.__name} ne peut pas évoluer davantage.")

    def get_pokemon_info(self, name):
        try:
            with open('pokemon.json', 'r') as f :
                pokemon_data = json.load(f)
                for pokemon in pokemon_data:
                    if pokemon['name'] == name:
                        return pokemon['types'], pokemon.get('evolution', None)
        except FileNotFoundError:
            print("Fichier pokemon.json non trouvé.")
        return[], None

    # Getters :
    def get_name(self):
        return self.__name
    
    def get_type(self):
        return self.__type
    
    def get_level(self):
        return self.__level
    
    def get_hp(self):
        return self.__hp
    
    def get_speed(self):
        return self.__speed
    
    def get_attack(self):
        return self.__attack
    
    def get_defence(self):
        return self.__defence
    
    def get_evolution(self):
        return self.__evolution
    
    # Setters
    def set_hp(self, hp):
        self.__hp = hp
    

