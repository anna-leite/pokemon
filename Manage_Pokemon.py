import sys
import json
import pygame
import os
from classPokemon import Pokemon
from classCombat import Combat
from classManagePokemons import managePokemon

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
player = "anna"
search_pokemon = 0
pokemon_data = []
selected_pokemon_images = [None, None, None]  # To hold selected Pokémon images
available_pokemon = [pokemon for pokemon in pokemon_data if pokemon.get('available', False)]  # Filter available Pokémon

# Initialize pygame and create the window.
pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Choose your team")

# Placeholder image for Pokémon.
placeholder_image = pygame.Surface((150, 150), pygame.SRCALPHA)
placeholder_image.fill((0, 0, 0))

info_font = pygame.font.Font(FONT, 30)
clock = pygame.time.Clock()

# Load Pokémon data from the JSON file
pokeball_file = f"{player}_pokeball.json"  # change to {player_name}_pokeball.json later on
pokemon_data = load_pokemon_data(pokeball_file)

# Render the first Pokémon.
pokemon_display_data = render_pokemon(pokemon_data, search_pokemon)

# Create buttons.
prev_button = Button("< Previous", (SCREEN_WIDTH * 0.375, SCREEN_HEIGHT * 0.9), SCREEN_WIDTH)
next_button = Button("Next >", (SCREEN_WIDTH * 0.625, SCREEN_HEIGHT * 0.9), SCREEN_WIDTH)
back_button = Button("Back to Menu", (SCREEN_WIDTH * 0.90, SCREEN_HEIGHT * 0.1), SCREEN_WIDTH)

# Create buttons for each slot
slot_buttons = [
    Button("Slot 1", (SCREEN_WIDTH * 0.29, SCREEN_HEIGHT // 2), SCREEN_WIDTH),
    Button("Slot 2", (SCREEN_WIDTH * 0.52, SCREEN_HEIGHT // 2), SCREEN_WIDTH),
    Button("Slot 3", (SCREEN_WIDTH * 0.75, SCREEN_HEIGHT // 2), SCREEN_WIDTH)
]

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

        # Handle slot button events
        for i, button in enumerate(slot_buttons):
            if button.handle_event(event):
                if available_pokemon:  # Check if available Pokémon
                    selected_pokemon_images[i] = load_pokemon_image(available_pokemon[search_pokemon]["name"])  # Assign Pokémon to the slot

        if back_button.handle_event(event):
            print("Back to menu")  # delete this later

    draw_vertical_gradient(window, (106, 183, 245), (107, 220, 69))

    # Display Pokémon image.
    if pokemon_display_data["image"]:
        img = pokemon_display_data["image"]
        width, height = img.get_size()
        scaled_img = pygame.transform.scale(img, (width * 1.6, height * 1.6))
        img_rect = scaled_img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200))
        window.blit(scaled_img, img_rect)
    else:
        window.blit(placeholder_image, placeholder_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200)))

    # Render Pokémon information text.
    display_text = f"{pokemon_display_data.get('id', '')} - {pokemon_display_data.get('name', '')}"
    text_surface = info_font.render(display_text, True, (170, 170, 170))
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, int(SCREEN_HEIGHT // 1.5) - 200))
    window.blit(text_surface, text_rect)

    # Draw selected Pokémon images in slots
    for i in range(3):
        slot_x = SCREEN_WIDTH * 0.2 + (i * 180)
        slot_y = SCREEN_HEIGHT * 0.7 - 100
        if selected_pokemon_images[i]:
            img = selected_pokemon_images[i]
            scaled_img = pygame.transform.scale(img, (150, 150))  # Scale to fit the slot
            window.blit(scaled_img, (slot_x, slot_y))
        else:
            # Use the available Pokémon image as a placeholder if no image is selected
            if available_pokemon:
                available_img = load_pokemon_image(available_pokemon[i]["name"])
                if available_img:
                    scaled_img = pygame.transform.scale(available_img, (150, 150))
                    window.blit(scaled_img, (slot_x, slot_y))  # Show available Pokémon image
            else:
                window.blit(placeholder_image, (slot_x, slot_y))  # Show placeholder if no image is selected

    # Draw buttons
    prev_button.draw(window)
    next_button.draw(window)
    back_button.draw(window)
    for button in slot_buttons:
        button.draw(window)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()