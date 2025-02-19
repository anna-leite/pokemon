import pygame
import sys

# Initialize Pygame
pygame.init()

pokemon = "squirtle"
damage = "damage"
defense = "defense"
level = "level"
# Constants
WIDTH = 800
HEIGHT = 600
FPS = 60
MAX_HEALTH = 100
FONT_PATH = "oxanium/Oxanium-Regular.ttf"
COLORS = {
    "BLACK": (0, 0, 0),
    "DARK_GREY": (68, 68, 68),
    "WHITE": (255, 255, 255),
    "RED": (255, 0, 0),
    "GREEN": (107, 220, 69),
    "LIGHT_GREY": (200, 200, 200, 10)
}
TEXT = {
    "NEW_OPPONENT": f"a wild {pokemon} has appeared",
    "SELECT": "Choose one of your pokemon to fight",
    "ATTACK": f"your attack does {damage} damage",
    "DEFENSE": f"you defend with {defense}, you take {damage} damage",
    "WIN": f"you win! You level increased to {level}",
    "LOSE": f"{pokemon} is dead, you have an empty pokemon slot",
}

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Combat")

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
    draw_rounded_rect(surface, COLORS["LIGHT_GREY"], background_rect, 10)

    # Draw the health bar background and current health
    draw_rounded_rect(surface, COLORS["RED"], (x, y, bar_length, 20), 10)
    draw_rounded_rect(surface, COLORS["GREEN"], (x, y, current_length, 20), 10)

    # Draw name and level
    font = pygame.font.Font(FONT_PATH, 24)
    name_surface = font.render(name, True, COLORS["BLACK"])
    level_surface = font.render(f"Level: {level}", True, COLORS["BLACK"])
    surface.blit(name_surface, (x, y - 30))  # Name above the bar
    surface.blit(level_surface, (x + bar_length - level_surface.get_width(), y + 25)) 
    
# # Function to display text with typing effect
# def display_typing_text(surface, text, y, speed):
#     typed_text = ""
#     for char in text:
#         typed_text += char
#         surface.blit(background_image, (0, 0)) 
        
#         # Render the text and center it
#         text_surface = font.render(typed_text, True, COLORS["BLACK"])
#         text_rect = text_surface.get_rect(center=(WIDTH // 2, y))  # Center the text
#         surface.blit(text_surface, text_rect)
        
#         pygame.display.flip() 
#         pygame.time.delay(speed) 
        
# Load images
def load_image(path, size):
    image = pygame.image.load(path)
    return pygame.transform.scale(image, size)

# Main game loop
clock = pygame.time.Clock()
background_image = load_image("Backgrounds/forest.png", (WIDTH, HEIGHT))
player_image = load_image("squirtle.png", (500, 500))
opponent_image = load_image("squirtle.png", (250, 250))

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
    screen.blit(player_image, (WIDTH // 16, HEIGHT // 2))
    screen.blit(opponent_image, (500, 260))

    # Draw health bars
    draw_health_bar(screen, 400, 500, player_health, MAX_HEALTH, "Player", 1, 400)
    draw_health_bar(screen, 300, 300, opponent_health, MAX_HEALTH, "Opponent", 1, 200)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
