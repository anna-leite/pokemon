import pygame

class Menu:
    def __init__(self, game):
        self.game = game

        # screen width & length
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2

        # booléen mis à True tant qu'on ne quitte pas le jeu
        self.run_display = True

        # curseur du jeu
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100

    def draw_cursor(self):
        self.game.draw_text("*", 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
            self.game.window.blit(self.game.display, (0, 0))
            pygame.display.update()
            self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"

        # positions à  adapter
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.addpokemonx, self.addpokemony = self.mid_w, self.mid_h + 60
        self.pokedexx, self.pokedexy = self.mid_w, self.mid_h + 90
        self.addplayerx, self.addplayery = self.mid_w, self.mid_h + 120
        self.quitx, self.quity = self.mid_w, self.mid_h + 150
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True

        # boucle True - tant qu'on ne quitte pas le jeu
        while self.run_display:

            # en gros il faut que dans la classe game
            # il y ait une fonction "check_events()"
            self.game.check_events()
            self.check_input()

            # à remplacer par l'image de background pour le menu
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("Menu principal", 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Lancer une partie", 20, self.startx, self.starty)
            self.game.draw_text("Ajouter un Pokemon", 20, self.addpokemonx, self.addpokemony)
            self.game.draw_text("Voir son Pokedex", 20, self.pokedexx, self.pokedexy)
            self.game.draw_text("Ajouter un joueur", 20, self.addplayerx, self.addplayery)
            self.game.draw_text("Quitter le jeu", 20, self.quitx, self.quity)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.addpokemonx + self.offset, self.addpokemony)
                self.state = "AddPokemon"
            elif self.state == "AddPokemon":
                self.cursor_rect.midtop = (self.pokedexx + self.offset, self.pokedexy)
                self.state = "Pokedex"
            elif self.state == "Pokedex":
                self.cursor_rect.midtop = (self.addplayerx + self.offset, self.addplayery)
                self.state = "AddPlayer"
            elif self.state == "AddPlayer":
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = "Quit"
            elif self.state == "Quit":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"
        elif self.game.UP_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = "Quit"
            if self.state == "AddPokemon":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"
            if self.state == "Pokedex":
                self.cursor_rect.midtop = (self.addpokemonx + self.offset, self.addpokemony)
                self.state = "AddPokemon"
            if self.state == "AddPlayer":
                self.cursor_rect.midtop = (self.pokedexx + self.offset, self.pokedexy)
                self.state = "Pokedex"
            if self.state == "Quit":
                self.cursor_rect.midtop = (self.addplayerx + self.offset, self.addplayery)
                self.state = "AddPlayer"

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == "Start":
                self.game.playing = True
            elif self.state == "AddPokemon":
                self.game.current_menu = self.game.add_pokemon
            elif self.state == "Pokedex":
                self.game.current_menu = self.game.pokedex
            elif self.state == "AddPlayer":
                self.game.current_menu = self.game.add_player
            elif self.state == "Quit":
                self.game.running = False


class AddPokemonMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

class PokedexMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

class AddPlayerMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
