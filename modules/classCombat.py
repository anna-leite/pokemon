from modules.classPokemon import Pokemon

class Combat:  
    def __init__(self, pokemon_player, pokemon_random):
        self.pokemon_player = pokemon_player
        self.pokemon_random = pokemon_random
        self.type_multiplier = {
                "acier": {"acier": 0.5, "dragon": 0.5, "fée": 0.5, "glace": 0.5, "insecte": 0.5, 
                        "normal": 0.5, "plante": 0.5, "psy": 0.5, "roche": 0.5, "vol": 0.5, 
                        "poison": 0, "combat": 2, "feu": 2, "sol": 2},

                "combat": {"insecte": 0.5, "roche": 0.5, "ténèbre": 0.5, 
                        "fée": 2, "psy": 2, "vol": 2},

                "dragon": {"eau": 0.5, "électrik": 0.5, "feu": 0.5, "plante": 0.5, 
                        "dragon": 2, "fée": 2, "glace": 2},

                "eau": {"acier": 0.5, "eau": 0.5, "feu": 0.5, "glace": 0.5, 
                        "électrik": 2, "plante": 2},

                "électrik": {"acier": 0.5, "électrik": 0.5, "vol": 0.5, 
                            "sol": 2},

                "fée": {"combat": 0.5, "insecte": 0.5, "ténèbre": 0.5, 
                        "dragon": 0, "acier": 2, "poison": 2},

                "feu": {"acier": 0.5, "fée": 0.5, "feu": 0.5, "glace": 0.5, "insecte": 0.5, "plante": 0.5, 
                        "eau": 2, "roche": 2, "sol": 2},

                "glace": {"glace": 0.5, 
                        "acier": 2, "combat": 2, "feu": 2, "roche": 2},

                "insecte": {"combat": 0.5, "plante": 0.5, "sol": 0.5, 
                            "feu": 2, "roche": 2, "vol": 2},

                "normal": {"spectre": 0, 
                        "combat": 2},

                "plante": {"eau": 0.5, "électrik": 0.5, "plante": 0.5, "sol": 0.5, 
                        "feu": 2, "glace": 2, "insecte": 2, "poison": 2, "vol": 2},

                "poison": {"combat": 0.5, "fée": 0.5, "insecte": 0.5, "plante": 0.5, "poison": 0.5, 
                        "psy": 2, "sol": 2},

                "psy": {"combat": 0.5, "psy": 0.5, 
                        "insecte": 2, "spectre": 2, "ténèbre": 2},

                "roche": {"feu": 0.5, "normal": 0.5, "poison": 0.5, "vol": 0.5, 
                        "acier": 2, "combat": 2, "eau": 2, "plante": 2, "sol": 2},

                "sol": {"poison": 0.5, "roche": 0.5, 
                        "électrik": 0, "eau": 2, "glace": 2, "plante": 2},

                "spectre": {"insecte": 0.5, "poison": 0.5, 
                            "combat": 0, "normal": 0, 
                            "spectre": 2, "ténèbre": 2},

                "ténèbre": {"spectre": 0.5, "ténèbre": 0.5, 
                            "psy": 0, "combat": 2, "fée": 2, "insecte": 2},

                "vol": {"combat": 0.5, "insecte": 0.5, "plante": 0.5, 
                        "sol": 0, "électrik": 2, "glace": 2, "roche": 2}
            }
        


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
        # ATTENTION DE BIEN RETOURNER LES VARIABLES POUR LEILA
        if winner == self.pokemon_player:
            winner.level_up()
            winner.evolve()
            
    

    


        
