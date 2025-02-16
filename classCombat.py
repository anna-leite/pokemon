class Combat:
    type_multiplier = {
        "acier" : {"acier dragon fee glace insecte normal plante psy roche vole" : "0.5", "poison" : "0", "combat feu sol" : "2"},
        "combat" : {"insect roche tenebre" : "0.5", "fee psy vol" : "2"},
        "dragon" : {"eau electrik feu plante" : "0.5", "dragon fee glace" : "2"},
        "eau" : {"acier eau feu glace" : "0.5", "electrik plante" : "2"},
        "electrik" : {"acier electrik vol" : "0.5", "sol" : "2"},
        "fee" : {"combat insecte tenebre" : "0.5", "dragon" : "0", "acier poison" : "2"},
        "feu" : {"acier fee feu glace insecte plante" : "0.5", "eau roche sol" : "2"}, 
        "glace" : {"glace" : "0.5", "acier combat feu roche" : "2"}, 
        "insecte" : {"combat plante sol" : "0.5", "feu roche vol" : "2"}, 
        "normal" : {"sepctre" : "0", "combat" : "2"}, 
        "plante" : {"eau electrik plante sol" : "0.5", "feu glace insecte poison vol" : "2"}, 
        "poison" : {"combat fee insecte plante poison" : "0.5", "psy sol" : "2"}, 
        "psy" : {"combat psy" : "0.5", "insecte spectre tenebre" : "2"}, 
        "roche" : {"feu normal poison vol" : "0.5", "acier combat eau plante sol" : "2"}, 
        "sol" : {"poison roche" : "0.5", "electrik" : "0", "eau glace plante" : "2"}, 
        "spectre" : {"insecte poison" : "0.5", "combat normal" : "0", "spectre tenebre" : "2"}, 
        "tenebre" : {"spectre tenebre" : "0.5", "psy" : "0", "combat fee insecte" : "2"}, 
        "vol" : {"combat insecte plante" : "0.5", "sol" : "0", "electrik glace roche" : "2"}, 
        }
    
    def __init__(self, pokemon_player, pokemon_random):
        self.pokemon_player = pokemon_player
        self.pokemon_random = pokemon_random

    def calculate_damage(self, attacker, defender):
        multiplier = 1
