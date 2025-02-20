import pygame
import json
import sys
import requests
from classCombat import combat
from Battle import draw_battle 

# Initialize Pygame
pygame.init()

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

def get_font_size(screen_width):
    return max(16, int(screen_width * 0.03))

# Load Pokedex
def load_pokedex():
    with open('pokedex.json') as f:
        return json.load(f)

# Create a new player's pokeball
def create_pokeball(name):
    starter_pokemon = [
        {"id": 24, "name": "Pikachu", "xp": 35, "hp": 35, "attack": 55, "defense": 51, "speed": 20, "types": ["", ""], "evolution": ""},
        {"id": 7, "name": "Squirtle", "xp": 35, "hp": 39, "attack": 52, "defense": 58, "speed": 16, "types": ["", ""], "evolution": ""},
        {"id": 1, "name": "Bulbasaur", "xp": 35, "hp": 45, "attack": 49, "defense": 59, "speed": 18, "types": ["", ""], "evolution": ""}
    ]
    with open(f'{name}_pokeball.json', 'w') as f:
        json.dump(starter_pokemon, f)

# Main Game Class
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pokémon Battle Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = "welcome"  # Welcome, Menu, Manage_pokemon, Pokedex, Pre-Battle, Battle, Win, Lose
        self.player_name = ""
        self.pokedex = load_pokedex()
        self.player_pokemon = []
        self.selected_pokemon = None # change to 3 starter pokemon by default. 

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if self.state == "welcome":
                    if event.key == pygame.K_RETURN:  # Simulate name entry
                        self.player_name = "Player"  # Replace code from Anna
                        create_pokeball(self.player_name)
                        self.state = "menu"
                elif self.state == "menu":
                    if event.key == pygame.K_1:  # Manage Pokémon
                        self.state = "manage_pokemon"
                    elif event.key == pygame.K_2:  # See Pokédex
                        self.state = "pokedex"
                    elif event.key == pygame.K_3:  # Go to Battle screens
                        self.state == "pre-battle"   
                elif self.state == "pre-battle":
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3]:  # Assuming 3 Pokémon
                        index = event.key - pygame.K_1  # Convert key to index (0, 1, 2)
                        if 0 <= index < len(self.player_pokemon):
                            self.selected_pokemon = self.player_pokemon[index]  # Select the Pokémon
                            self.state = "battle"  # Transition to battle state
                elif self.state == "battle":
                    # Simulate the battle outcome
                    winner = combat.pokemon_player(self.selected_pokemon)  # Call the combat function
                    if winner:  # If the player wins
                        self.state = "win"
                    else:  # If the player loses
                        self.state = "lose"
                elif self.state == "pokedex" or self.state == "manage_pokemon":
                    if event.key == pygame.K_ESCAPE:  # Go back to menu
                        self.state = "menu"
                elif event.key == pygame.K_4:  # Quit
                    self.running = False

    def update(self):
        pass  # Update game logic here

    def draw(self):
        self.screen.fill(COLOURS['WHITE'])
        if self.state == "welcome":
            self.draw_welcome()
        elif self.state == "menu":
            self.draw_menu()
        elif self.state == "pokedex":
            self.draw_pokedex()
        elif self.state == "manage_pokemon":
            self.draw_manage_pokemon()
        elif self.state == "pre-battle":
            self.draw_pre_battle()
        elif self.state == "battle":
            self.draw_battle()
        elif self.state == "win":
            self.draw_win()
        elif self.state == "lose":
            self.draw_lose()
        pygame.display.flip()

    def draw_welcome(self):
        font = pygame.font.Font(FONT_PATH, 74)
        text = font.render("Welcome to Pokemon Battle!", True, BLACK)
        self.screen.blit(text, (100, 100))
        # Add input for player name here
        # Morgane to complete

    def draw_menu(self):
        font = pygame.font.Font(None, 74)
        text = font.render("Menu", True, BLACK)
        self.screen.blit(text, (100, 100))
        # Display options
        options = ["1. Manage Pokemon", "2. See Pokedex", "3. Battle", "4. Quit"]
        for i, option in enumerate(options):
            option_text = font.render(option, True, BLACK)
            self.screen.blit(option_text, (100, 200 + i * 50))

    def draw_pokedex(self):
        font = pygame.font.Font(None, 36)
        title = font.render("Pokedex", True, BLACK)
        self.screen.blit(title, (100, 50))
        # take code from pokedex.py
        
        # Display all Pokémon in the Pokedex
        for i, pokemon in enumerate(self.pokedex):
            pokemon_text = font.render(f"{i + 1}. {pokemon['name']}", True, BLACK)
            self.screen.blit(pokemon_text, (100, 100 + i * 30))
        
        # Instructions to go back
        back_text = font.render("Press ESC to go back", True, BLACK)
        self.screen.blit(back_text, (100, SCREEN_HEIGHT - 50))

    def draw_manage_pokemon(self):
        font = pygame.font.Font(None, 36)
        title = font.render("Manage Pokemon", True, BLACK)
        self.screen.blit(title, (100, 50))
        
        # Load player's Pokémon from the JSON file
        try:
            with open(f'{self.player_name}_pokeball.json') as f:
                self.player_pokemon = json.load(f)
        except FileNotFoundError:
            self.player_pokemon = []

        # Display player's Pokémon
        for i, pokemon in enumerate(self.player_pokemon):
            pokemon_text = font.render(f"{i + 1}. {pokemon['name']}", True, BLACK)
            self.screen.blit(pokemon_text, (100, 100 + i * 30))
        
        # Instructions to go back
        back_text = font.render("Press ESC to go back", True, BLACK)
        self.screen.blit(back_text, (100, SCREEN_HEIGHT - 50))

    def draw_pre_battle(self):
        font = pygame.font.Font(FONT_PATH, 36)
        background_image = "Assets/Images/Backgrounds/forest.png"
        pokemon_image_path = f"Assets/Images/Pokemon/{random_pokemon_name}_front.png"
        
        # Draw background
        screen.blit(background_image, (0, 0))
        # A random pokemon appears
        title = font.render(f"A {random_pokemon} has appeared", True, COLOURS['BLACK'])
        self.screen.blit(title, (100, 50))
        # draw pokemon using image
        screen.blit(pokemon_image_path, (100, 100))
        
        # Display player's Pokémon to choose from
        
        for i, pokemon in enumerate(self.player_pokemon):
            pokemon_text = font.render(f"{i + 1}. {pokemon['name']}", True, COLOURS['BLACK'])
            self.screen.blit(pokemon_text, (100, 100 + i * 30))
        
        # Instructions to select a Pokémon
        instructions = font.render("Choose a Pokémon to fight", True, COLOURS['BLACK'])
        self.screen.blit(instructions, (100, SCREEN_HEIGHT - 100))
        

    def draw_battle(self):
        font = pygame.font.Font(None, 36)
        title = font.render("Battle!", True, BLACK)
        self.screen.blit(title, (100, 50))
        # turn-based attack/defense combat game loop until player wins or loses
        # transition to win or lose screen
        
    def draw_win(self):
        font = pygame.font.Font(None, 36)
        title = font.render("You won the battle!", True, BLACK)
        self.screen.blit(title, (100, 50))
        
        # Instructions to go back to menu
        back_text = font.render("Back to menu", True, BLACK)
        self.screen.blit(back_text, (100, SCREEN_HEIGHT - 50))
        
    def draw_lose(self):
        font = pygame.font.Font(None, 36)
        title = font.render("You lost the battle!", True, BLACK)
        self.screen.blit(title, (100, 50))
        # Instructions to go back to menu
        back_text = font.render("Back to menu", True, BLACK)
        self.screen.blit(back_text, (100, SCREEN_HEIGHT - 50))
            
# Start the game
if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
