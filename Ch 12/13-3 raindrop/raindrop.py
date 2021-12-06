#13-3 Raindrops
import sys, pygame
from pygame.sprite import Sprite


class Settings:
        def __init__(self):
            #screen settings.
            self.bg_color = (0, 0, 0)
class Rainpic(Sprite):
        def __init__(self, ai_game):
            super().__init__()
            self.screen = ai_game.screen
            self.screen_rect = ai_game.screen.get_rect()
            

            self.image = pygame.image.load('raindrop.bmp')
            self.rect = self.image.get_rect()

            self.rect.x = self.rect.width
            self.rect.y = self.rect.height

            self.x = float(self.rect.x)
            self.y = float(self.rect.y)

            self.rain_speed = 0.5
        def update(self):
            #rain falls
            self.y  += self.rain_speed
            self.rect.y = self.y
class Raindrop:

        def __init__(self):
            pygame.init()
            self.settings = Settings()
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.screen_width = self.screen.get_rect().width
            self.screen_height = self.screen.get_rect().height
            pygame.display.set_caption("Raindrops")
            self.rainpics =  pygame.sprite.Group()
            self.create_drops()
        def run_drops(self):
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                         if event.key == pygame.K_q:
                                pygame.quit()
                                sys.exit()
                self.screen.fill(self.settings.bg_color)
                self.rainpics.draw(self.screen)
                self.rainpics.update()
                pygame.display.flip()        
        def create_drops(self):
            #drop the bass
            rain = Rainpic(self)
            rain_width, rain_height = rain.rect.size
            available_space_x = self.screen_width - (2*rain_width)
            number_rain_x = available_space_x // (2*rain_width)

            available_space_y = (self.screen_height - (4*rain_height))
            number_rows = available_space_y // (2*rain_height)
            
            for row_number in range(number_rows):
                for rain_drops in range(number_rain_x):
                    self.create_drop_fleet(rain_drops, row_number)
        def create_drop_fleet(self, rain_drops, row_number):
            rain = Rainpic(self)
            rain_width, rain_height = rain.rect.size
            rain.x = rain_width + 2 * rain_width * rain_drops
            rain.rect.x = rain.x
            rain.rect.y = rain.rect.height + 2 * rain.rect.height*row_number
            rain.rect.y = rain.y
            self.rainpics.add(rain)         
if __name__ == '__main__':
    ai = Raindrop()
    ai.run_drops()
