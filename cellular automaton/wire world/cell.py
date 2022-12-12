import pygame
from colors import WHITE, YELLOW, BLUE, RED


class Cell:
    def __init__(self, row, col, width, height):
        self.row = row
        self.col = col
        
        self.width = width
        self.height = height

        self.x = col * width
        self.y = row * width

        self.color = WHITE

    def is_empty(self):
        return self.color == WHITE
    
    def is_wire(self):
        return self.color == YELLOW
    
    def is_signal(self):
        return self.color == BLUE

    def is_tail(self):
        return self.color == RED

    def make_empty(self):
        self.color = WHITE
    
    def make_wire(self):
        self.color = YELLOW
    
    def make_signal(self):
        self.color = BLUE

    def make_tail(self):
        self.color = RED

    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def __repr__(self):
        if self.is_empty():
            return 'W'
        elif self.is_wire():
            return 'Y'
        elif self.is_signal():
            return 'B'
        elif self.is_tail():
            return 'R'
