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

def draw_win(self):
    font = pygame.font.Font(None, 36)
    title = font.render("You won the battle!", True, BLACK)
    self.screen.blit(title, (100, 50))
    
    # Instructions to go back to menu
    back_text = font.render("Back to menu", True, BLACK)
    self.screen.blit(back_text, (100, SCREEN_HEIGHT - 50))