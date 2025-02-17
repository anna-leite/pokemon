from game import Game

pokegame = Game()

while pokegame.running:
    pokegame.curr_menu.display_menu()
    pokegame.game_loop()