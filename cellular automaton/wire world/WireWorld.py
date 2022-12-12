import pygame
import time
from grid import Grid
from constants import WIDTH, HEIGHT, ROWS, COLS, CELL_WIDTH, CELL_HEIGHT, MOORE_NEIGHBORHOOD, VON_NEUMANN_NEIGHBORHOOD
from colors import WHITE


class WireWorld:
    def __init__(self):
        self.grid = Grid(ROWS, COLS)

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.cell_type = 1
        self.neighborhood = MOORE_NEIGHBORHOOD
        self.__runner = True
        self.start = False

    def get_clicked_pos(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos

        row = mouse_y // CELL_HEIGHT
        col = mouse_x // CELL_WIDTH

        return row, col

    def process_input(self):
        mouse_pos = pygame.mouse.get_pos()
        row, col = self.get_clicked_pos(mouse_pos)

        if pygame.mouse.get_pressed()[0]:
            if self.cell_type == 1:
                self.grid[row][col].make_wire()
            
            elif self.cell_type == 2:
                self.grid[row][col].make_signal()
            
            elif self.cell_type == 3:
                self.grid[row][col].make_tail()
        
        elif pygame.mouse.get_pressed()[2]:
            self.grid[row][col].make_empty()

    def update(self):
        self.grid.update(self.neighborhood)

    def render(self):
        self.screen.fill(WHITE)
        self.grid.render(self.screen)
        
        pygame.display.flip()

    def run(self):
        while self.__runner:
            self.clock.tick(45)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__runner = False
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.start = not self.start
                    
                    elif event.key == pygame.K_r:
                        self.update()
                    
                    elif event.key == pygame.K_1:
                        self.cell_type = 1
                    
                    elif event.key == pygame.K_2:
                        self.cell_type = 2
                    
                    elif event.key == pygame.K_3:
                        self.cell_type = 3

            self.process_input()
            if self.start:
                self.update()
                time.sleep(0.15)
            self.render()

        
        pygame.quit()


# WireWorld().run()
