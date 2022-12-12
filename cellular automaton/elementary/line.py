import pygame
from cell import Cell
from constants import LINE_WIDTH, LINE_HEIGHT, LENGTH, CELL_WIDTH, CELL_HEIGHT
from colors import GREY


class Line:
    def __init__(self, line=None, epoch=0, length=LENGTH, width=LINE_WIDTH, height=LINE_HEIGHT):
        self.width = width
        self.height = height
        
        self.length = length
        self.epoch = epoch

        self.line = []
        if line is None:
            for idx in range(length):
                cell = Cell(0, idx, width=CELL_WIDTH, height=CELL_HEIGHT)
                self.line.append(cell)
        else:
            self.line = line

    def render(self, screen):
        for cell in self.line:
            cell.render(screen)
        
        pygame.draw.line(screen, GREY, (0, self.epoch * CELL_HEIGHT), (self.width, self.epoch * CELL_HEIGHT))   # horizontal

        for idx in range(1, self.length):
            pygame.draw.line(screen, GREY, (idx * CELL_WIDTH, self.epoch * self.height), (idx * CELL_WIDTH, (self.epoch + 1) * self.height))    # vertical
    
    def __getitem__(self, key):
        return self.line[key]
    
    def __repr__(self):
        return f'Line({str(self.line)})'
