import sys
import requests
import pygame


# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FONT = "oxanium/Oxanium-Regular.ttf"
BLACK = (0, 0, 0)
DARK_GREY = (68, 68, 68)
WHITE = (255, 255, 255)
POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/"
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


# draw a vertical gradient background.
def draw_vertical_gradient(surface, top_color, bottom_color):
    height = surface.get_height()
    for y in range(height):
        ratio = y / height
        r = top_color[0] + (bottom_color[0] - top_color[0]) * ratio
        g = top_color[1] + (bottom_color[1] - top_color[1]) * ratio
        b = top_color[2] + (bottom_color[2] - top_color[2]) * ratio
        pygame.draw.line(surface, (int(r), int(g), int(b)), (0, y), (surface.get_width(), y))


# API logic (synchronous fetching)
def fetch_pokemon(pokemon):
    url = f"{POKEAPI_URL}{pokemon}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print("Error fetching data:", e)
    return None

def render_pokemon(pokemon_identifier):
    data = fetch_pokemon(pokemon_identifier)
    if data:
        # Get the animated sprite URL.
        sprite_url = (data.get("sprites", {})
                        .get("versions", {})
                        .get("generation-v", {})
                        .get("black-white", {})
                        .get("animated", {})
                        .get("front_default", None))
        if sprite_url:
            try:
                image_resp = requests.get(sprite_url)
                image_bytes = image_resp.content
                temp_filename = "temp_pokemon.png"
                with open(temp_filename, "wb") as f:
                    f.write(image_bytes)
                image = pygame.image.load(temp_filename).convert_alpha()
            except Exception as e:
                print("Error loading image:", e)
                image = None
        else:
            image = None
        return {"name": data["name"], "id": data["id"], "image": image, "not_found": False}
    else:
        return {"name": "not found :(", "id": "", "image": None, "not_found": True}


# Global state.
search_pokemon = 1
pokemon_data = {
    "name": "",
    "id": "",
    "image": None,
    "not_found": False
}

# Initialize pygame and create the window.
pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pokédex")

try:
    pokedex_image = pygame.image.load("./img/pokedexm.png").convert_alpha()
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


# Create buttons.
prev_button = Button("< Previous", (SCREEN_WIDTH * 0.375, SCREEN_HEIGHT * 0.9), SCREEN_WIDTH)
next_button = Button("Next >", (SCREEN_WIDTH * 0.58, SCREEN_HEIGHT * 0.9), SCREEN_WIDTH)

# Render the first Pokémon.
pokemon_data = render_pokemon(search_pokemon)


# Main loop.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check button events.
        if prev_button.handle_event(event):
            if search_pokemon > 1:
                search_pokemon -= 1
                pokemon_data = render_pokemon(search_pokemon)
        if next_button.handle_event(event):
            search_pokemon += 1
            pokemon_data = render_pokemon(search_pokemon)

    draw_vertical_gradient(window, (106, 183, 245), (107, 220, 69))
    window.blit(pokedex_image, pokedex_rect)

    # Display Pokémon image.
    if pokemon_data["image"]:
        img = pokemon_data["image"]
        # Double the size of the Pokémon image.
        width, height = img.get_size()
        scaled_img = pygame.transform.scale(img, (width * 1.6, height * 1.6))
        # Adjust the image rectangle to center the scaled image.
        img_rect = scaled_img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        window.blit(scaled_img, img_rect)
    else:
        window.blit(placeholder_image, placeholder_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))

    # Render Pokémon information text.
    display_text = f"{pokemon_data.get('id', '')} - {pokemon_data.get('name', '')}"
    text_surface = info_font.render(display_text, True, (170, 170, 170))
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, int(SCREEN_HEIGHT // 1.5)))
    window.blit(text_surface, text_rect)

    prev_button.draw(window)
    next_button.draw(window)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()