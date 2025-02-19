import pygame
import sys
import json

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
MAX_HEALTH = 100
FONT_PATH = "Assets/Fonts/Oxanium-Regular.ttf"

COLOURS = {
    "BLACK": (0, 0, 0),
    "DARK_GREY": (68, 68, 68),
    "WHITE": (255, 255, 255),
    "RED": (255, 0, 0),
    "GREEN": (107, 220, 69),
    "LIGHT_GREY": (200, 200, 200, 10)
}

TEXT = {
    "ATTACK": f"your attack does {damage} damage",
    "DEFENSE": f"you defend with {defense}, you take {damage} damage",
}

FONT_SIZE = 28
BOX_PADDING = 5

# variables
player_pokemon = ""
random_pokemon = ""
damage = "damage"
defense = "defense"
level = "level"

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battle!")

# Initialize Pygame
pygame.init()

# Function to draw the text box
def draw_text_box(text, x, y):
    # Split the text into lines
    words = text.split(' ')
    current_line = ""
    lines = []
    
    for word in words:
        # Check if adding the next word exceeds the width
        test_line = current_line + word + ' '
        text_surface = font.render(test_line, True, COLOURS["COLOURS["WHITE"]"])
        if text_surface.get_width() > WIDTH - 40:  # 20 padding on each side
            lines.append(current_line)
            current_line = word + ' '
        else:
            current_line = test_line
            
    # Add the last line if it exists
    if current_line:
        lines.append(current_line)

    # Calculate the box size based on the number of lines
    text_box_width = max(font.render(line, True, COLOURS["COLOURS["WHITE"]"]).get_width() for line in lines) + BOX_PADDING * 2
    text_box_height = len(lines) * (FONT_SIZE + BOX_PADDING) + BOX_PADDING

    # Create a surface for the box with transparency
    box_surface = pygame.Surface((text_box_width, text_box_height), pygame.SRCALPHA)
    box_surface.fill(COLOURS["GREY"])

    # Draw the box
    pygame.draw.rect(box_surface, COLOURS["WHITE"], (0, 0, text_box_width, text_box_height), 2)

    # Blit the box and text onto the screen
    screen.blit(box_surface, (x, y))
    
    # Draw each line of text
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, COLOURS["WHITE"])
        screen.blit(text_surface, (x + BOX_PADDING, y + BOX_PADDING + i * (FONT_SIZE + BOX_PADDING)))

# Health variables
player_health = MAX_HEALTH
opponent_health = MAX_HEALTH

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

def draw_battle(self):
        clock = pygame.time.Clock()
        background_image = load_image("Backgrounds/forest.png", (SCREEN_WIDTH, SCREEN_HEIGHT))
        player_image = load_image("{player_pokemon_name}.png", (500, 500))
        opponent_image = load_image("{random_pokemon_name}.png", (250, 250))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Update health
            player_health = max(0, player_health - 0.05)
            opponent_health = max(0, opponent_health - 0.03)

            # Draw background
            screen.blit(background_image, (0, 0))
            
            # # Display the text
            # display_typing_text(screen, TEXT["NEW_OPPONENT"], 50, 100)  # 100ms delay

            # Draw Pokémon images
            screen.blit(player_image, (SCREEN_WIDTH // 16, SCREEN_HEIGHT // 2))
            screen.blit(opponent_image, (500, 260))

            # Draw health bars
            draw_health_bar(screen, 400, 500, player_health, MAX_HEALTH, "Player", 1, 400)
            draw_health_bar(screen, 300, 300, opponent_health, MAX_HEALTH, "Opponent", 1, 200)

            # Update the display
            pygame.display.flip()

            # Cap the frame rate
            clock.tick(FPS)
