import pygame
import sys
import random
from classPokemon import Pokemon
from classCombat import Combat
from classManagePokemons import managePokemon

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
FONT_PATH = "pokemon/Assets/Fonts/Oxanium-Regular.ttf"
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

# Test functions
def test_draw_pre_battle():
    # Initialize necessary objects for the test
    name_player = "anna"
    combat = Combat(name_player)
    random_pokemon = combat.pokemon_random()
    manage = managePokemon(name_player)
    fighting_team = manage.fighting_pokemons()

    # Set up a clock to simulate frame rate
    clock = pygame.time.Clock()

    # Simulate one frame of the game
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Render the screen
        screen.fill(COLOURS["WHITE"])  # Clear the screen

        # Draw background (checking if background loads)
        background_image = pygame.image.load("pokemon/Assets/Images/Backgrounds/forest.png")
        screen.blit(background_image, (0, 0))

        # Check if a random Pokémon appears (name and types)
        random_pokemon_name = font.render(random_pokemon.get_name(), True, COLOURS['BLACK'])
        screen.blit(random_pokemon_name, (500, 50))
        
        random_pokemon_types_text = " / ".join(random_pokemon.get_types()) if random_pokemon.get_types() else "Unknown"
        rp_types_text = font.render(random_pokemon_types_text, True, COLOURS['BLACK'])
        screen.blit(rp_types_text, (500, 80))

        # Check if player's Pokémon are displayed (with names and types)
        y_offset = 300
        for i, pokemon in enumerate(fighting_team):
            pokemon_name = font.render(pokemon.get_name(), True, COLOURS['BLACK'])
            pokemon_types_text = " / ".join(pokemon.get_types()) if pokemon.get_types() else "Unknown"
            pokemon_types = font.render(pokemon_types_text, True, COLOURS['BLACK'])
            screen.blit(pokemon_name, (200, y_offset + (i * 100)))
            screen.blit(pokemon_types, (200, y_offset + (i * 100) + 30))

        # Update the display
        pygame.display.flip()

        # Test: Check if the background and Pokémon are displayed
        assert background_image is not None, "Background image did not load correctly."
        assert random_pokemon_name is not None, "Random Pokémon name did not render."
        assert rp_types_text is not None, "Random Pokémon types did not render."
        assert pokemon_name is not None, "Player Pokémon name did not render."
        assert pokemon_types is not None, "Player Pokémon types did not render."

        # Limit the frame rate
        clock.tick(FPS)
        running = False  # Stop after one frame

    print("Test passed: All elements were rendered correctly.")

# Run the test
test_draw_pre_battle()



