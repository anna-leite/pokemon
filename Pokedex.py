import sys
import json
import pygame
import os

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FONT = "Assets/Fonts/Oxanium-Regular.ttf"
BLACK = (0, 0, 0)
DARK_GREY = (68, 68, 68)
WHITE = (255, 255, 255)
FPS = 60

def get_font_size(screen_width):
    return max(16, int(screen_width * 0.03))

# Custom Button
class Button:
    def __init__(self, text, center, screen_width):
        self.text = text
        self.screen_width = screen_width
        self.width = screen_width * 0.18          
        self.padding = screen_width * 0.03

        font_size = get_font_size(screen_width)
        self.normal_font = pygame.font.Font(FONT, font_size)
        self.active_font = pygame.font.Font(FONT, int(font_size * 0.9))

        self.text_normal = self.normal_font.render(self.text, True, WHITE)
        self.text_active = self.active_font.render(self.text, True, WHITE)

        self.height = self.text_normal.get_height() + 2 * self.padding
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = center

        self.border_width = 2
        self.border_radius = 5
        self.is_pressed = False

    def draw(self, surface):
        pygame.draw.rect(surface, DARK_GREY, self.rect, border_radius=self.border_radius)
        pygame.draw.rect(surface, BLACK, self.rect, self.border_width, border_radius=self.border_radius)
        text_surface = self.text_active if self.is_pressed else self.text_normal
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.is_pressed = True
                return False
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.is_pressed:
                self.is_pressed = False
                if self.rect.collidepoint(event.pos):
                    return True
        return False

# Draw a vertical gradient background.
def draw_vertical_gradient(surface, top_color, bottom_color):
    height = surface.get_height()
    for y in range(height):
        ratio = y / height
        r = top_color[0] + (bottom_color[0] - top_color[0]) * ratio
        g = top_color[1] + (bottom_color[1] - top_color[1]) * ratio
        b = top_color[2] + (bottom_color[2] - top_color[2]) * ratio
        pygame.draw.line(surface, (int(r), int(g), int(b)), (0, y), (surface.get_width(), y))

# Load Pokémon data from JSON file
def load_pokemon_data(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        return data["pokemon"]  # Return the list of Pokémon

def load_pokemon_image(name):
    image_path = f"Assets/Images/Pokemon/{name}_front.png"
    if os.path.exists(image_path):
        return pygame.image.load(image_path).convert_alpha()
    else:
        print(f"Image not found: {image_path}")
        return None

def render_pokemon(pokemon_data, index):
    if 0 <= index < len(pokemon_data):
        pokemon = pokemon_data[index]
        image = load_pokemon_image(pokemon["name"])
        return {
            "name": pokemon["name"],
            "id": pokemon["id"],
            "image": image,
            "not_found": False
        }
    else:
        return {"name": "not found :(", "id": "", "image": None, "not_found": True}

# Global state.
search_pokemon = 0
pokemon_data = []

# Initialize pygame and create the window.
pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pokédex")

try:
    pokedex_image = pygame.image.load("Assets/Images/Pokedex/pokedex.png").convert_alpha()
except Exception as e:
    print("Could not load pokedex image:", e)
    pokedex_image = pygame.Surface((300, 300))
    pokedex_image.fill((200, 200, 200))
pokedex_rect = pokedex_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

# Placeholder image for Pokémon.
placeholder_image = pygame.Surface((150, 150), pygame.SRCALPHA)
placeholder_image.fill((255, 0, 0))

info_font = pygame.font.Font(FONT, 30)
clock = pygame.time.Clock()

# Load Pokémon data from the JSON file
pokedex_file = "pokedex.json"
pokemon_data = load_pokemon_data(pokedex_file)

# Render the first Pokémon.
pokemon_display_data = render_pokemon(pokemon_data, search_pokemon)

# Create buttons.
prev_button = Button("< Previous", (SCREEN_WIDTH * 0.375, SCREEN_HEIGHT * 0.9), SCREEN_WIDTH)
next_button = Button("Next >", (SCREEN_WIDTH * 0.58, SCREEN_HEIGHT * 0.9), SCREEN_WIDTH)
back_button = Button("Back to Menu", (SCREEN_WIDTH * 0.90, SCREEN_HEIGHT * 0.1), SCREEN_WIDTH)

# Main loop.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check button events.
        if prev_button.handle_event(event):
            if search_pokemon > 0:
                search_pokemon -= 1
                pokemon_display_data = render_pokemon(pokemon_data, search_pokemon)
        if next_button.handle_event(event):
            if search_pokemon < len(pokemon_data) - 1:
                search_pokemon += 1
                pokemon_display_data = render_pokemon(pokemon_data, search_pokemon)
        if back_button.handle_event(event):
            handle_events.state = "menu" # fix this when added to main.py

    draw_vertical_gradient(window, (106, 183, 245), (107, 220, 69))
    window.blit(pokedex_image, pokedex_rect)

    # Display Pokémon image.
    if pokemon_display_data["image"]:
        img = pokemon_display_data["image"]
        width, height = img.get_size()
        scaled_img = pygame.transform.scale(img, (width * 1.6, height * 1.6))
        img_rect = scaled_img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        window.blit(scaled_img, img_rect)
    else:
        window.blit(placeholder_image, placeholder_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))

    # Render Pokémon information text.
    display_text = f"{pokemon_display_data.get('id', '')} - {pokemon_display_data.get('name', '')}"
    text_surface = info_font.render(display_text, True, (170, 170, 170))
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, int(SCREEN_HEIGHT // 1.5)))
    window.blit(text_surface, text_rect)

    prev_button.draw(window)
    next_button.draw(window)
    back_button.draw(window)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()