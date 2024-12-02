import pygame # type: ignore
from settings import *


def draw_graph(surface, array, highlites, x, y, w, h):

    for i, n in enumerate(array):
        colour = RECT_COLOUR[highlites[i]]
        pygame.draw.rect(surface, colour, pygame.Rect((x-w*len(array))//2+(i*w), y-(n+1)*h, w, (n+1)*h))