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
FONT = "oxanium/Oxanium-Regular.ttf"

COLOURS = {
    "BLACK": (0, 0, 0),
    "DARK_GREY": (68, 68, 68),
    "WHITE": (255, 255, 255),
    "RED": (255, 0, 0),
    "GREEN": (107, 220, 69),
    "LIGHT_GREY": (200, 200, 200, 10)
}

def draw_pre_battle(self):
        font = pygame.font.Font(None, 36)
        title = font.render("Select Your Pokémon", True, COLOURS['BLACK'])
        self.screen.blit(title, (100, 50))
        
        # Display player's Pokémon to choose from
        for i, pokemon in enumerate(self.player_pokemon):
            pokemon_text = font.render(f"{i + 1}. {pokemon['name']}", True, COLOURS['BLACK'])
            self.screen.blit(pokemon_text, (100, 100 + i * 30))
        
        # Instructions to select a Pokémon
        instructions = font.render("Press 1, 2, or 3 to select a Pokémon", True, COLOURS['BLACK'])
        self.screen.blit(instructions, (100, SCREEN_HEIGHT - 100))
        
        # Instructions to go back
        back_text = font.render("Press ESC to go back", True, COLOURS['BLACK'])
        self.screen.blit(back_text, (100, SCREEN_HEIGHT - 50))