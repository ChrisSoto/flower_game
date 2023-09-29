import pygame
import sys
from student import *

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720


class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Flowers')
        self.display_surface = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.display_surface.fill('white')
        self.clock = pygame.time.Clock()
        # self.petal = pygame.image.load('graphics/petal.png')
        self.background = pygame.image.load('graphics/Sky.png')
        self.ledge = pygame.image.load('graphics/brick_ledge.png')

    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.display_surface.blit(self.background, (0, 0))
            self.display_surface.blit(self.ledge, (0, 0))
            studentWork(self.display_surface)
            # self.petal.fill((190, 50, 100, 100),
            #                 special_flags=pygame.BLEND_MIN)
            # self.display_surface.blit(self.petal, (0, 0))
            pygame.display.update()


if __name__ == '__main__':
    main = Main()
    main.run()
