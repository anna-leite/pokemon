import pygame


# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DEFAULT_SIZE_FULLSCREEN = (SCREEN_WIDTH, SCREEN_HEIGHT)
FPS = 60
FONT = "Assets/Fonts/Oxanium-Regular.ttf"

BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
LIGHTBLUE = (153, 235, 255, 0.5)
BACKGROUND = pygame.image.load("capture.png")
image = pygame.transform.scale(BACKGROUND, DEFAULT_SIZE_FULLSCREEN)
POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/"


font = pygame.font.Font(None, 74)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

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
                elif event.key == pygame.K_RETURN :
                    return user_text
                else :
                    user_text += event.unicode


        screen.blit(image, (0, 0))
        text = font.render("Welcome to Pokemon Battle!", True, BLACK)
        screen.blit(text, (100, 75))

        text_surface = font.render(user_text, True, BLACK)

        pygame.draw.rect(screen, LIGHTBLUE, (100, 200, 500, 100))
        screen.blit(text_surface, (150, 220))
        


        pygame.display.flip()

draw_welcome()