#12 -1 blue sky.py

import pygame
import sys
class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0 , 0 , 255)

class BlueScreen:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("12-1 Blue Screen")

    def run_program(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    ai = BlueScreen()
    ai.run_program()
