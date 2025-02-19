import pygame
import sys
import json

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

TEXT = {
    "TRAIN": "Select 3 pokémon to train",
    "DISPLAY_STATS": f"{name} is a {type} type, xp {base_experience}, {speed} speed, {attack} attack and {defense} defense",
    "SELECTION": f"You have chosen{pokemon_name}"
}

FONT_SIZE = 28
BOX_PADDING = 5

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Battle")

# Initialize Pygame
pygame.init()

# Function to draw the text box
def draw_text_box(text, x, y):
    # Split the text into lines
    words = text.split(' ')
    current_line = ""
    lines = []
    font = pygame.font.Font(FONT_PATH, 36)
    
    for word in words:
        # Check if adding the next word exceeds the width
        test_line = current_line + word + ' '
        text_surface = font.render(test_line, True, COLOURS["WHITE"])
        if text_surface.get_width() > SCREEN_WIDTH - 40:  # 20 padding on each side
            lines.append(current_line)
            current_line = word + ' '
        else:
            current_line = test_line
            
    # Add the last line if it exists
    if current_line:
        lines.append(current_line)

    # Calculate the box size based on the number of lines
    text_box_width = max(font.render(line, True, COLOURS["WHITE"]).get_width() for line in lines) + BOX_PADDING * 2
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

def draw_manage_pokemon(self):
        clock = pygame.time.Clock()
        font = pygame.font.Font(FONT_PATH, 36)
        background_image = "Assets/Images/Backgrounds/beach.png"
        pokemon_image_path = f"Assets/Images/Pokemon/{random_pokemon_name}_front.png"
        
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
            # Draw background
            screen.blit(background_image, (0, 0))
                        
            # draw pokeball and pokemon on top (from {name}_pokeball.json)
            # draw prev/next buttons (leila to code)
            # take {name}_front.png path using {name}_pokeball.json name value (anna)
            # click selection event
            
            # code anna pour 3 pokemon to select/train
            # function to draw 3 pokemon using starter pokemon, or avalaible booleen inside {name}_pokeball.json
            screen.blit(pokemon_1_image_path, (100, 100))
            screen.blit(pokemon_2_image_path, (300, 100))
            screen.blit(pokemon_3_image_path, (500, 100))
            
            # Display player's 3 available slots Pokémon to choose from
            # anna pour creer choix de 3 pokemon avec types

            pokemon_name_1 = font.render(f"{pokemon_1_name}{type}", True, COLOURS['BLACK'])
            self.screen.blit(instructions, (100, SCREEN_HEIGHT - 100))
            pokemon_name_2 = font.render(f"{pokemon_2_name}{type}", True, COLOURS['BLACK'])
            self.screen.blit(instructions, (100, SCREEN_HEIGHT - 100))
            pokemon_name_3 = font.render(f"{pokemon_3_name}{type}", True, COLOURS['BLACK'])
            self.screen.blit(instructions, (100, SCREEN_HEIGHT - 100))
            
            # Instructions
            def instruction():
                draw_text_box(TEXT['TRAIN'], (x, y)):
                
            # Update the display
            pygame.display.flip()

            # Cap the frame rate
            clock.tick(FPS)
            