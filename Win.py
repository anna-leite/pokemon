import sys
import pygame

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

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Battle Result")
    clock = pygame.time.Clock()

    # Create button
    button = Button("Back to Menu", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50), SCREEN_WIDTH)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if button.handle_event(event):
                print("Going back to menu...") # delete this later!
                # handle_event.menu 

        # Draw background
        draw_vertical_gradient(screen, (106, 183, 245), (107, 220, 69))

        # Draw text
        font_size = get_font_size(SCREEN_WIDTH)
        font = pygame.font.Font(FONT, font_size)
        text_surface = font.render("You won the battle", True, WHITE)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(text_surface, text_rect)

        # Draw button
        button.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()