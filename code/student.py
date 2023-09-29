from pygame import Surface
from arranger import *

top_shelf = 390
bottom_shelf = 500

location = {}
location[1] = (300, top_shelf)
location[2] = (600, top_shelf)
location[3] = (900, top_shelf)


def student_work(surface: Surface):
    big_pot = get_pot('big')
    flower_1 = make_flower(stem_idx='c', flower_idx='b')
    place_pot(surface, big_pot, flower_1, location[1])

    small_pot = get_pot('sml')
    flower_2 = make_flower(stem_idx='a', flower_idx='c')
    place_pot(surface, small_pot, flower_2, location[2])

    small_pot = get_pot('med')
    flower_2 = make_flower(stem_idx='c', flower_idx='d')
    place_pot(surface, small_pot, flower_2, location[3])
