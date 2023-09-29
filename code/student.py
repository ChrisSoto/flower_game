from pygame import Surface
from arranger import *

location = {}
location[1] = (300, 273)


def studentWork(surface: Surface):
    bigPot = getPot('big')
    flower = makeFlower('a', 'a', 'a', (0, 0, 0))
    placePot(surface, bigPot, flower, location[1])
