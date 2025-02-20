import pygame
import sys
import json
import random
from classPokemon import Pokemon
from classCombat import Combat
from classManagePokemons import managePokemon

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
FONT_PATH = "Assets/Fonts/Oxanium-Regular.ttf"
COLOURS = {
    "BLACK": (0, 0, 0),
    "DARK_GREY": (68, 68, 68),
    "WHITE": (255, 255, 255),
    "RED": (255, 0, 0),
    "GREEN": (107, 220, 69),
    "LIGHT_GREY": (200, 200, 200, 10)
}

FONT_SIZE = 28
BOX_PADDING = 5

pygame.init()
font = pygame.font.Font(FONT_PATH, 36)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Battle")

player = "anna"


# Function to draw the text box
def draw_text_box(text, x, y):
    words = text.split(' ')
    current_line = ""
    lines = []
    
    for word in words:
        test_line = current_line + word + ' '
        text_surface = font.render(test_line, True, COLOURS["WHITE"])
        if text_surface.get_width() > SCREEN_WIDTH - 40:
            lines.append(current_line)
            current_line = word + ' '
        else:
            current_line = test_line
            
    if current_line:
        lines.append(current_line)

    text_box_width = max(font.render(line, True, COLOURS["WHITE"]).get_width() for line in lines) + BOX_PADDING * 2
    text_box_height = len(lines) * (FONT_SIZE + BOX_PADDING) + BOX_PADDING

    box_surface = pygame.Surface((text_box_width, text_box_height), pygame.SRCALPHA)
    box_surface.fill(COLOURS["DARK_GREY"])

    pygame.draw.rect(box_surface, COLOURS["WHITE"], (0, 0, text_box_width, text_box_height), 2)

    screen.blit(box_surface, (x, y))
    
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, COLOURS["WHITE"])
        screen.blit(text_surface, (x + BOX_PADDING, y + BOX_PADDING + i * (FONT_SIZE + BOX_PADDING)))


def draw_pre_battle():
    TEXT = {
        "NEW_OPPONENT": "A wild Pokémon has appeared!",
        "SELECT": "Choose one of your Pokémon to fight!",
    }

    clock = pygame.time.Clock()
    background_image = pygame.image.load("Assets/Images/Backgrounds/forest.png")
    
    combat = Combat(player)
    pokeball = managePokemon(player)
    fighting_team = pokeball.fighting_pokemons()
    combat.get_player_pokemon("pikachu")
    random_pokemon = combat.generate_random_pokemon(fighting_team)
    random_pokemon_image = pygame.image.load(f"Assets/Images/Pokemon/{random_pokemon.get_name()}_front.png")
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(background_image, (0, 0))

        
        # Draw random Pokémon
        screen.blit(random_pokemon_image, (500, 100))
        random_pokemon_name = font.render(random_pokemon.get_name(), True, COLOURS['BLACK'])
        screen.blit(random_pokemon_name, (500, 50))

        # Draw random Pokémon types
        random_pokemon_types_text = " / ".join(random_pokemon.get_types()) if random_pokemon.get_types() else "Unknown"
        rp_types_text = font.render(random_pokemon_types_text, True, COLOURS['BLACK'])
        screen.blit(rp_types_text, (500, 80))

        # Draw the text box
        draw_text_box(TEXT['NEW_OPPONENT'], SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT - 150)

        # Display player's Pokémon
        y_offset = 300
        for i, pokemon in enumerate(fighting_team):
            # Pokémon image
            pokemon_image = pygame.image.load(f"Assets/Images/Pokemon/{pokemon}_front.png")
            screen.blit(pokemon_image, (100, y_offset + (i * 100)))

            # Pokémon name
            pokemon_name = font.render(pokemon, True, COLOURS['BLACK'])
            screen.blit(pokemon_name, (200, y_offset + (i * 100)))

            # Pokémon types
            pokemon_types_text = " / ".join(Pokemon(pokemon).get_types()) if Pokemon(pokemon).get_types() else "Unknown"
            pokemon_types = font.render(pokemon_types_text, True, COLOURS['BLACK'])
            screen.blit(pokemon_types, (200, y_offset + (i * 100) + 30))

        # Display instructions
        instructions = font.render(TEXT['SELECT'], True, COLOURS['BLACK'])
        screen.blit(instructions, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT - 50))

        # ecrire l'événement qui récupère le clic de souris et qui enregistre le pokémon du joueur dans pokemon_player
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        # puis battle screen
        # player_pokemon = get_player_pokemon(pokemon cliqué)


        pygame.display.flip()
        clock.tick(FPS)

# Call the function to start the battle scene
draw_pre_battle()
            