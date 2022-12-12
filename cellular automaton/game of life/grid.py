import pygame
from cell import Cell
from constants import WIDTH, HEIGHT, ROWS, COLS, CELL_WIDTH, CELL_HEIGHT
from colors import WHITE, GREY, BLACK
from fonts import FONT


class Grid:
    def __init__(self, rows=ROWS, cols=COLS, width=WIDTH, height=HEIGHT):
        self.width = width
        self.height = height
        
        self.rows = rows
        self.cols = cols

        self.grid = []
        for row in range(rows):
            self.grid.append([])
            for col in range(cols):
                cell = Cell(row, col, width=CELL_WIDTH, height=CELL_HEIGHT)
                self.grid[row].append(cell)

    def neighbors_count(self, row, col, neighborhood):
        counter = 0
        for j, i in neighborhood:
            cell = self.grid[(row+i) % self.rows][(col+j) % self.cols]
            if cell.is_alive():
                counter += 1
        
        return counter

    def update(self, rules, neighborhood):
        new_grid = []
        for row in range(self.rows):
            new_grid.append([])
            for col in range(self.cols):
                cell = self.grid[row][col]
                neighbors_count = self.neighbors_count(row, col, neighborhood)
                
                new_cell = Cell(row, col, width=CELL_WIDTH, height=CELL_HEIGHT)
                new_cell.color = cell.color

                if cell.is_dead() and neighbors_count in rules[0]:
                    new_cell.make_alive()
                elif cell.is_alive() and neighbors_count not in rules[1]:
                    new_cell.make_dead()

                new_grid[row].append(new_cell)
        
        self.grid = new_grid

    def render(self, screen, neighborhood, rules, render_count=False):
        for row in self.grid:
            for cell in row:
                # if cell.color == BLACK:
                cell.render(screen)

                if render_count:
                    neighbors_count = self.neighbors_count(cell.row, cell.col, neighborhood)
                    if cell.is_alive() and neighbors_count not in rules[1]:
                        text_surf = FONT.render(f'{neighbors_count}', True, WHITE)
                    
                    elif cell.is_dead() and neighbors_count in rules[0]:
                        text_surf = FONT.render(f'{neighbors_count}', True, BLACK)
                    
                    else:
                        text_surf = FONT.render(f'{neighbors_count}', True, GREY)
                    
                    screen.blit(text_surf, (cell.x + (cell.width - text_surf.get_width()) // 2, cell.y + (cell.height - text_surf.get_height()) // 2))

        for row in range(1, self.rows):
            pygame.draw.line(screen, GREY, (0, row * CELL_HEIGHT), (self.width, row * CELL_HEIGHT))   # horizontal

        for col in range(1, self.cols):
            pygame.draw.line(screen, GREY, (col * CELL_WIDTH, 0), (col * CELL_WIDTH, self.height))    # vertical
    
    def __getitem__(self, key):
        return self.grid[key]
