import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu")
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


# Menu loop function
def draw_menu():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                # Vérification des clics
                if 120 <= mouse_x <= 520 and 200 <= mouse_y <= 280:
                    # Lancer une partie (tu devras créer la fonction)
                    print("Manage Pokemon")
#                    manage_pokemon()
                elif 120 <= mouse_x <= 520 and 300 <= mouse_y <= 380:
                    # Ajouter un Pokémon (tu devras créer la fonction)
                    print("See Pokedex")
#                    see_pokedex()
                elif 120 <= mouse_x <= 520 and 400 <= mouse_y <= 480:
                    # Voir le Pokédex (tu devras créer la fonction)
                    print("Battle")
#                    battle()
#                elif 400 <= mouse_x <= 800 and 750 <= mouse_y <= 850:
#                    return
#                elif 400 <= mouse_x <= 800 and 900 <=mouse_y <= 1000:
#                    pygame.quit()
#                    sys.exit()

        screen.blit(image, (0, 0))
        pygame.draw.rect(screen, LIGHTBLUE, (120, 10, 600, 90))        
        pygame.draw.rect(screen, LIGHTBLUE, (450, 50, 00, 100))
        draw_text("Welcome to Pokemon Battle!", FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
        draw_button("Manage Pokemon", 120, 200, 400, 80)
        draw_button("See Pokedex", 120, 300, 400, 80)
        draw_button("Battle", 120, 400, 400, 80)
#        draw_button("Retour", 120, 500, 400, 80)
#        draw_button("Quit", 400, 900, 400, 100)

        pygame.display.flip()


if __name__ == "__main__":
    draw_menu()


"""

Explications :

    Menus : Chaque fonction (main_menu(), game_menu(), add_player()) représente un menu.
      Quand un bouton est cliqué, la fonction correspondante est appelée.
    Menu principal : Les boutons permettent de choisir entre "Menu du jeu" et "Ajouter un joueur".
    Menu du jeu : Dans ce menu, les boutons permettent de lancer une partie, ajouter un Pokémon, voir le Pokédex, ou quitter le jeu.
    Ajouter un joueur : Une fois cliqué, tu pourrais afficher un champ pour que l’utilisateur saisisse un nom ou d’autres informations.

Prochaines étapes :

    Lancer une partie : Tu peux créer une nouvelle fonction pour démarrer le jeu.
    Ajouter un Pokémon : Ajoute une fonction pour permettre l'ajout d'un Pokémon.
    Pokédex : Crée une fonction qui affiche les Pokémon que le joueur a ajoutés.

Cela te donne une bonne base pour construire ton jeu. Si tu veux plus de détails ou des fonctionnalités spécifiques, fais-le moi savoir !

"""

