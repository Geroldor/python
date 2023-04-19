import pygame
from pygame import *


class nave:
    def __init__(self, font_Type, font_Size, font_Color, font, posicx, posicy, speed):
        self.font_builded = font.SysFont(font_Type, font_Size)
        self.font = self.font_builded.render(font, True, font_Color)
        self.posicx = posicx
        self.posicy = posicy
        self.speed = speed
    
    