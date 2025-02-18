import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 1500, 1200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu Principal")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Police
font = pygame.font.SysFont("Arial", 40)

# Fonction pour afficher le texte
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Fonction pour créer un bouton
def draw_button(text, x, y, width, height):
    pygame.draw.rect(screen, GRAY, (x, y, width, height))
    draw_text(text, font, BLACK, screen, x + width // 2, y + height // 2)

# Fonction du menu principal
def main_menu():
    while True:
        screen.fill(WHITE)

        # Affichage des options du menu principal
        draw_text("Menu Principal", font, BLACK, screen, WIDTH // 2, 100)
        draw_button("Menu du Jeu", 350, 400, 500, 100)
        draw_button("Ajouter un Joueur", 350, 600, 500, 100)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                # Vérification des clics
                if 350 <= mouse_x <= 850 and 400 <= mouse_y <= 500:
                    game_menu()
                elif 350 <= mouse_x <= 850 and 600 <= mouse_y <= 700:
                    add_player()

# Fonction du menu du jeu
def game_menu():
    while True:
        screen.fill(WHITE)

        # Affichage des options du menu du jeu
        draw_text("Menu du Jeu", font, BLACK, screen, WIDTH // 2, 100)
        draw_button("Lancer une Partie", 400, 300, 400, 100)
        draw_button("Gérer les Pokémons", 400, 450, 400, 100)
        draw_button("Voir le Pokédex", 400, 600, 400, 100)
        draw_button("Retour", 400, 750, 400, 100)
        draw_button("Quitter", 400, 900, 400, 100)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                # Vérification des clics
                if 400 <= mouse_x <= 800 and 300 <= mouse_y <= 400:
                    # Lancer une partie (tu devras créer la fonction)
                    print("Lancer une partie")
                elif 400 <= mouse_x <= 800 and 450 <= mouse_y <= 550:
                    # Ajouter un Pokémon (tu devras créer la fonction)
                    print("Gérer les Pokémons")
                elif 400 <= mouse_x <= 800 and 600 <= mouse_y <= 700:
                    # Voir le Pokédex (tu devras créer la fonction)
                    print("Voir le Pokédex")
                elif 400 <= mouse_x <= 800 and 750 <= mouse_y <= 850:
                    return
                elif 400 <= mouse_x <= 800 and 900 <=mouse_y <= 1000:
                    pygame.quit()
                    sys.exit()

# Fonction pour ajouter un joueur
def add_player():
    while True:
        screen.fill(WHITE)
        
        draw_text("Ajouter un Joueur", font, BLACK, screen, WIDTH // 2, 100)

        # Ici tu peux ajouter des champs pour saisir le nom du joueur, par exemple
        draw_button("Retour", 250, 200, 300, 60)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if 250 <= mouse_x <= 550 and 200 <= mouse_y <= 260:
                    return  # Retourner au menu principal

if __name__ == "__main__":
    main_menu()


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