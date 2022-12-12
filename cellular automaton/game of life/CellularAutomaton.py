import pygame
from grid import Grid
from constants import WIDTH, HEIGHT, ROWS, COLS, CELL_WIDTH, CELL_HEIGHT, MOORE_NEIGHBORHOOD, VON_NEUMANN_NEIGHBORHOOD
from colors import WHITE


class CellularAutomaton:
    def __init__(self, rules=((3,), (2, 3))):
        self.rules = rules
        self.grid = Grid(ROWS, COLS)

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.render_count = False
        self.neighbor_mode = False
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
            if self.neighbor_mode:
                self.grid[row][col].make_neighbor()    
            else:
                self.grid[row][col].make_alive()
        elif pygame.mouse.get_pressed()[2]:
            self.grid[row][col].make_dead()

    def update(self):
        self.grid.update(self.rules, self.neighborhood)

    def render(self):
        self.screen.fill(WHITE)
        self.grid.render(self.screen, self.neighborhood, self.rules, self.render_count)
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
                    
                    elif event.key == pygame.K_f:
                        self.render_count = not self.render_count
                    
                    elif event.key == pygame.K_n:
                        self.neighbor_mode = not self.neighbor_mode
                    
                    elif event.key == pygame.K_c:
                        if self.neighborhood == MOORE_NEIGHBORHOOD:
                            self.neighborhood = VON_NEUMANN_NEIGHBORHOOD
                        
                        else:
                            self.neighborhood = MOORE_NEIGHBORHOOD

            self.process_input()
            if self.start:
                self.update()
            self.render()
        
        pygame.quit()


# rules = ((3,), (2, 3))
# CellularAutomaton(rules).run()
