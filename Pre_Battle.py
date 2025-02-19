import pygame
import json
import sys
import requests
from classCombat import combat
from Battle import draw_battle 

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
FONT_PATH = "oxanium/Oxanium-Regular.ttf"

COLOURS = {
    "BLACK": (0, 0, 0),
    "DARK_GREY": (68, 68, 68),
    "WHITE": (255, 255, 255),
    "RED": (255, 0, 0),
    "GREEN": (107, 220, 69),
    "LIGHT_GREY": (200, 200, 200, 10)
}

def draw_pre_battle(self):
        font = pygame.font.Font(FONT_PATH, 36)
        background_image = "Assets/Images/Backgrounds/forest.png"
        pokemon_image_path = f"Assets/Images/Pokemon/{random_pokemon_name}_front.png"
        
        # Draw background
        screen.blit(background_image, (0, 0))
        # A random pokemon appears
        title = font.render(f"A {random_pokemon} has appeared", True, COLOURS['BLACK'])
        self.screen.blit(title, (100, 50))
        # draw pokemon using image
        screen.blit(pokemon_image_path, (100, 100))
        
        # Display player's Pokémon to choose from
        
        for i, pokemon in enumerate(self.player_pokemon):
            pokemon_text = font.render(f"{i + 1}. {pokemon['name']}", True, COLOURS['BLACK'])
            self.screen.blit(pokemon_text, (100, 100 + i * 30))
        
        # Instructions to select a Pokémon
        instructions = font.render("Choose a Pokémon to fight", True, COLOURS['BLACK'])
        self.screen.blit(instructions, (100, SCREEN_HEIGHT - 100))
        
        