import pygame
import sys
import classManagePokemons
import Menu
from classManagePokemons import managePokemon

# Initialisation de Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Welcome")
FPS = 60
FONT_PATH = "Assets/Fonts/Oxanium-Regular.ttf"
FONT = pygame.font.Font(FONT_PATH, 40)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
LIGHTBLUE = (153, 235, 255, 0.5)
BACKGROUND = pygame.image.load("Assets/Images/Backgrounds/pikachu.png")
image = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Fonction pour afficher le texte
def draw_text(text, FONT, color, surface, x, y):
    textobj = FONT.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Fonction pour créer un bouton
def draw_button(text, x, y, SCREEN_width, height):
    pygame.draw.rect(screen, LIGHTBLUE, (x, y, SCREEN_width, height))
    draw_text(text, FONT, BLACK, screen, x + SCREEN_width // 2, y + height // 2)

def draw_welcome():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    user_text = ""

    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER) :
#                    player = managePokemon(user_text)
#                    player.load_pokemon()
#                    print(player.player_name)
#                    print(player.pokemon_list)

                    """
                    on doit avoir : player = user_text
                    pokeball = managePokemon(player).load_pokemon()
                    
                    """
 #                   print("pressed")
#                    return user_text
                else :
                    user_text += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos                
                if (100 <= mouse_x <= 600 and 400 <= mouse_y <= 500) and user_text != "" :
                    player = managePokemon(user_text)
                    player.load_pokemon()
                    Menu.draw_menu()

        screen.blit(image, (0, 0))
        text = FONT.render("Welcome to Pokemon Battle!", True, BLACK)
        screen.blit(text, (100, 75))

        text_surface = FONT.render(user_text, True, BLACK)

        pygame.draw.rect(screen, LIGHTBLUE, (100, 200, 500, 100))
        pygame.draw.rect(screen, LIGHTBLUE, (100, 400, 500, 100))
        draw_button("Menu principal", 100, 400, 500, 100)
        screen.blit(text_surface, (150, 220))

        pygame.display.flip()

draw_welcome()