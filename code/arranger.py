import pygame
import random
from pygame import Surface

pots = {}
pots['sml'] = pygame.image.load('graphics/pot_sml.png')
pots['med'] = pygame.image.load('graphics/pot_med.png')
pots['big'] = pygame.image.load('graphics/pot_big.png')

stem = {}
stem['a'] = pygame.image.load('graphics/stem_a.png')
stem['b'] = pygame.image.load('graphics/stem_b.png')
stem['c'] = pygame.image.load('graphics/stem_c.png')

flower = {}
flower['a'] = pygame.image.load('graphics/flower_a.png')
flower['b'] = pygame.image.load('graphics/flower_b.png')
flower['c'] = pygame.image.load('graphics/flower_c.png')
flower['d'] = pygame.image.load('graphics/flower_d.png')
flower['e'] = pygame.image.load('graphics/flower_e.png')
flower['f'] = pygame.image.load('graphics/flower_f.png')
flower['g'] = pygame.image.load('graphics/flower_g.png')
flower['h'] = pygame.image.load('graphics/flower_h.png')
flower['i'] = pygame.image.load('graphics/flower_i.png')
flower['j'] = pygame.image.load('graphics/flower_j.png')
flower['k'] = pygame.image.load('graphics/flower_k.png')
flower['l'] = pygame.image.load('graphics/flower_l.png')
flower['m'] = pygame.image.load('graphics/flower_m.png')
flower['n'] = pygame.image.load('graphics/flower_n.png')


def make_flower(stem_idx: str, flower_idx, color=(255, 255, 255, 100)) -> Surface:
    width = 167
    height = 200

    stem_image = stem[stem_idx]
    stem_image.fill((106, 166, 122, 100), special_flags=pygame.BLEND_MIN)

    flower_image = flower[flower_idx]
    flower_image.fill(color, special_flags=pygame.BLEND_MIN)

    stem_width, stem_height = stem_image.get_size()
    holder = pygame.Surface((width, height))
    holder = pygame.Surface((width, height), pygame.SRCALPHA, 32)
    holder = holder.convert_alpha()
    holder.blit(stem_image, (width/2 - stem_width/2, height - stem_height))
    holder.blit(flower_image, (0, 0))
    return holder


def place_pot(surface: Surface, pot: Surface, flower: Surface, location: ()):
    pot_width, pot_height = pot.get_size()
    flower_width = flower.get_width()
    flower_height = flower.get_height()

    flower_x = location[0] + pot_width/2 - flower_width/2
    flower_y = location[1] - pot_height - flower_height

    surface.blit(flower, (flower_x, flower_y))
    surface.blit(pot, (location[0], location[1] - pot_height))


def get_pot(size: str) -> Surface:
    return pots[size]


# def rotate(img, pos, angle):
#     w, h = img.get_size()
#     img2 = pygame.Surface((w*2, h*2), pygame.SRCALPHA)
#     img2.blit(img, (w-pos[0], h-pos[1]))
#     return pygame.transform.rotate(img2, angle)

# def makeFlowerPetals(petal: Surface, number_of_petals: int, size: int) -> Surface:
#     p_width = petal.get_width()
#     p_height = petal.get_height()
#     holder = pygame.Surface((size, size))
#     holder.fill((100, 0, 0, 1))
#     angle = 360/number_of_petals
#     last_angle = 0
#     new_angle = 0
#     for p in range(number_of_petals):
#         next_petal = petal.copy()
#         new_angle = angle + last_angle
#         # next_petal = rotate(next_petal, (size/2 - p_width /
#         #                     2, size/2 - p_height), new_angle)
#         next_petal = rotate(next_petal, (0, 0), new_angle)
#         holder.blit(next_petal, (0, 0))
#         last_angle = new_angle

#     return holder
