# In Space Fight, the player will control a ship that appears at the bottom right of the screen.
# The player can move the ship right and left using the arrow keys and shoot bullets using using the spacebar.
# When the game begins, a fleet of aliens fills the sky and moves across and down the screen.
# The player shoots and destroys the aliens.
# If the player shoots all the aliens, a new fleet appears that moves faster than the previous fleet.
# If any aliens hits the player's ship or reaches the bottom of the screen, the player loses a ship.
# If the player loses three ships, the game ends.

import sys
import pygame
from settings import Settings

# overall class to manage game assets and behavior
class SpaceFight:

    # initializes the game, and create game resources 
    def _init_(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(self.settings.screen_width, self.settings.screen_height)
        pygame.display.set_caption("Space Fight")
        self.bg_color = (230, 230, 230)
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    self.screen.fill(self.settings.bg_color)

            pygame.display.flip()
if _name_ == '_sf_':
    sf = SpaceFight()
    sf.run_game()