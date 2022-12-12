import pygame
from colors import WHITE, BLACK, LIGHT_BLUE


class Cell:
    def __init__(self, row, col, width, height):
        self.row = row
        self.col = col
        
        self.width = width
        self.height = height

        self.x = col * width
        self.y = row * width

        self.color = WHITE

    def is_dead(self):
        return self.color == WHITE
    
    def is_alive(self):
        return self.color == BLACK

    def make_dead(self):
        self.color = WHITE
    
    def make_alive(self):
        self.color = BLACK

    def make_neighbor(self):
        self.color = LIGHT_BLUE

    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def __repr__(self):
        if self.is_dead():
            return 'W'
        elif self.is_alive():
            return 'B'
