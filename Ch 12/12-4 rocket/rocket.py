import sys
import pygame
from pygame.sprite import Sprite

class Rocket: 
    def __init__(self):
        pygame.init()
        self.bg_color = (230,230,230)
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        pygame.display.set_caption("Rocket Mover 9000")
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
            # play button mouse stuff
    def _check_keydown_events(self,event):
        if event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            print ("moving right")
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        pygame.display.flip()
if __name__ == '__main__':
    ai = Rocket()
    ai.run_game()
    
