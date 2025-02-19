import unittest
import json
import os
from classPokemon import Pokemon
from classManagePokemons import managePokemon
from classCombat import Combat

class TestPokemonSystem(unittest.TestCase):
    
    def setUp(self):
        """Initialisation des objets avant chaque test."""
        self.player_name = "test_player"
        self.pokemon1 = Pokemon("pikachu")
        self.pokemon2 = Pokemon("bulbasaur")
        self.pokemon3 = Pokemon("squirtle")
        self.manager = managePokemon(self.player_name)
        self.combat = Combat(self.player_name)

    def test_pokemon_initialization(self):
        """Test de l'initialisation d'un Pokémon."""
        self.assertEqual(self.pokemon1.get_name(), "pikachu")
        self.assertGreater(self.pokemon1.get_hp(), 0)
        self.assertGreater(self.pokemon1.get_attack(), 0)

    def test_pokemon_damage(self):
        """Test des dégâts reçus par un Pokémon."""
        initial_hp = self.pokemon1.get_hp()
        self.pokemon1.take_damage(10)
        self.assertEqual(self.pokemon1.get_hp(), max(0, initial_hp - 10))

    def test_pokemon_evolution(self):
        """Test de l'évolution d'un Pokémon."""
        self.pokemon1.level_up()
        self.pokemon1.evolve()
        self.assertIsInstance(self.pokemon1.get_evolution(), (str, type(None)))

    def test_manage_pokemon(self):
        """Test de la gestion des Pokémon."""
        self.manager.add_pokemon(self.pokemon1)
        self.assertIn("pikachu", self.manager.list_pokemon())
        
        self.manager.remove_pokemon("pikachu")
        self.assertNotIn("pikachu", self.manager.list_pokemon())

    def test_update_availability(self):
        """Test de la mise à jour de la disponibilité des Pokémon."""
        self.manager.add_pokemon(self.pokemon1)
        self.manager.update_availability("pikachu", True)
        self.assertTrue(self.pokemon1.get_available())

    def test_combat_initialization(self):
        """Test de l'initialisation d'un combat."""
        self.assertIsNotNone(self.combat.pokemon_random)
        self.assertIsNotNone(self.combat.pokemon_player)

    def test_combat_execution(self):
        """Test d'un combat entre deux Pokémon."""
        winner = self.combat.battle()
        self.assertTrue(winner.is_alive())

if __name__ == "__main__":
    unittest.main()