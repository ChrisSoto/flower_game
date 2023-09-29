import pygame
from pygame import Surface

pots = {}
pots['sml'] = pygame.image.load('graphics/small_pot.png')
pots['med'] = pygame.image.load('graphics/med_pot.png')
pots['big'] = pygame.image.load('graphics/big_pot.png')

stem = {}
stem['a'] = pygame.image.load('graphics/stem_a.png')
stem['b'] = pygame.image.load('graphics/stem_b.png')
stem['c'] = pygame.image.load('graphics/stem_c.png')

seed = {}
seed['a'] = pygame.image.load('graphics/seed_a.png')
seed['b'] = pygame.image.load('graphics/seed_b.png')
seed['c'] = pygame.image.load('graphics/seed_c.png')
seed['d'] = pygame.image.load('graphics/seed_d.png')

petal = {}
petal['a'] = pygame.image.load('graphics/petal_a.png')
petal['b'] = pygame.image.load('graphics/petal_b.png')
petal['c'] = pygame.image.load('graphics/petal_c.png')


# def addFlowers(pot: Surface, flowers: Surface) -> Surface:
#     pot_width = pot.get_width()
#     flowers_width = flowers.get_width()
#     pot.blit(flowers, (pot_width/2 - flowers_width/2, 0))
#     return pot


def makeFlower(stemIdx: str, seedIdx: str, petalIdx: str, color=(0, 0, 0)) -> Surface:
    width = 150
    height = 200
    seed_width = seed[seedIdx].get_width()
    seed_height = seed[seedIdx].get_height()
    stem_width = stem[stemIdx].get_width()
    stem_height = stem[stemIdx].get_height()
    holder = pygame.Surface((width, height))
    # holder = pygame.Surface((width, height), pygame.SRCALPHA, 32)
    # holder = holder.convert_alpha()

    holder.blit(stem[stemIdx], (width/2 - stem_width/2, height - stem_height))
    holder.blit(seed[seedIdx], (width/2 - seed_width/2, seed_height/2))
    return holder


def placePot(surface: Surface, pot: Surface, flower: Surface, location: ()):
    pot_width = pot.get_width()
    pot_height = pot.get_height()
    flower_width = flower.get_width()
    flower_height = flower.get_height()

    flower_x = location[0] + pot_width/2 - flower_width/2
    flower_y = location[1] - flower_height

    surface.blit(flower, (flower_x, flower_y))
    surface.blit(pot, location)


def getPot(size: str) -> Surface:
    return pots[size]
