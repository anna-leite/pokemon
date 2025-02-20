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



font = pygame.font.Font(FONT_PATH, 36)

# Function to draw rounded rectangles
def draw_rounded_rect(surface, color, rect, radius):
    pygame.draw.rect(surface, color, rect, border_radius=radius)

# Function to draw the health bar
def draw_health_bar(surface, x, y, health, max_health, name, level, bar_length):
    health_ratio = health / max_health
    current_length = bar_length * health_ratio

    # Calculate dimensions for the background rectangle
    background_rect = (x - 10, y - 40, bar_length + 20, 70)  # Adjusted for padding
    draw_rounded_rect(surface, COLOURS["LIGHT_GREY"], background_rect, 10)

    # Draw the health bar background and current health
    draw_rounded_rect(surface, COLOURS["RED"], (x, y, bar_length, 20), 10)
    draw_rounded_rect(surface, COLOURS["GREEN"], (x, y, current_length, 20), 10)

    # Draw name and level
    font = pygame.font.Font(FONT_PATH, 24)
    name_surface = font.render(name, True, COLOURS["BLACK"])
    level_surface = font.render(f"Level: {level}", True, COLOURS["BLACK"])
    surface.blit(name_surface, (x, y - 30))  # Name above the bar
    surface.blit(level_surface, (x + bar_length - level_surface.get_width(), y + 25)) 

def load_image(path, size):
    image = pygame.image.load(path)
    return pygame.transform.scale(image, size)



def draw_battle():
        combat = Combat(player) 
        pokeball = managePokemon(player)
        fighting_team = pokeball.fighting_pokemons()
        combat.get_player_pokemon("pikachu")
        combat.generate_random_pokemon(fighting_team)
        clock = pygame.time.Clock()

        background_image = load_image("Assets/Images/Backgrounds/forest.png", (SCREEN_WIDTH, SCREEN_HEIGHT))
        player_pokemon_image = load_image(f"Assets/Images/Pokemon/{combat.player_pokemon.get_name()}_back.png", (500, 500))
        random_pokemon_image = load_image(f"Assets/Images/Pokemon/{combat.random_pokemon.get_name()}_front.png", (250, 250))

        # Health variables
        player_max_health = combat.player_pokemon.get_hp()
        random_max_health = combat.random_pokemon.get_hp()


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()



            # Draw background
            screen.blit(background_image, (0, 0))

            attacker, defender = combat.attacks_first()


            while combat.player_pokemon.is_alive() and combat.random_pokemon.is_alive():
                attacker_damage = combat.calculate_damage(attacker, defender)
                combat.perform_attack(attacker, defender)
                TEXT = {
        "ATTACK": f"{attacker.get_name()} does {attacker_damage} damage",
        "DEFENSE": f"{defender.get_name()} defends with {defender.get_defense()}, it takes {attacker_damage} damage",
    }
                draw_text_box(TEXT['ATTACK'], SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT - 150)
                draw_text_box(TEXT['DEFENSE'], SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT - 150)

                draw_health_bar(screen, 400, 500, combat.player_pokemon.get_hp(), player_max_health, f"{combat.player_pokemon.get_name()}", 1, 400)
                draw_health_bar(screen, 300, 300, combat.random_pokemon.get_hp(), random_max_health, f"{combat.random_pokemon.get_name()}", 1, 200)

                if not defender.is_alive():
                    winner = attacker
                    if winner == combat.player_pokemon :
                        winner.level_up()
                        winner.evolve()
                        pokeball.add_pokemon(combat.random_pokemon)
                        # win screen
                    elif winner == combat.random_pokemon :
                        pokeball.remove_pokemon(combat.player_pokemon)
                        # game over screen
                    
                attacker, defender = defender, attacker

            # Draw Pokémon images
            screen.blit(player_pokemon_image, (SCREEN_WIDTH // 16, SCREEN_HEIGHT // 2))
            screen.blit(random_pokemon_image, (500, 260))




            # Update the display
            pygame.display.flip()

            # Cap the frame rate
            clock.tick(FPS)

draw_battle()
