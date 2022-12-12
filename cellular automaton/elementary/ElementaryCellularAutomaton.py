import pygame
from cell import Cell
from line import Line
from constants import WIDTH, HEIGHT, EPOCHS, CELL_WIDTH, CELL_HEIGHT
from colors import GREY


class ElementaryCellularAutomaton:
    def __init__(self, rule):
        self.rule = '{0:08b}'.format(rule)
        self.rules = {
            (1, 1, 1): int(self.rule[0]),
            (1, 1, 0): int(self.rule[1]),
            (1, 0, 1): int(self.rule[2]),
            (1, 0, 0): int(self.rule[3]),
            (0, 1, 1): int(self.rule[4]),
            (0, 1, 0): int(self.rule[5]),
            (0, 0, 1): int(self.rule[6]),
            (0, 0, 0): int(self.rule[7])
        }
        self.line = Line()
        self.grid = [self.line]

        self.epoch = 0
        self.max_epochs = EPOCHS

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.__runner = True
        self.start = False
    
    def check_rule(self, cells):
        rule = tuple(map(lambda cell: int(cell.is_alive()), cells))
        return self.rules[rule]

    def get_clicked_pos(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos

        epoch = mouse_y // CELL_HEIGHT
        idx = mouse_x // CELL_WIDTH

        return epoch, idx

    def process_input(self):
        mouse_pos = pygame.mouse.get_pos()
        epoch, idx = self.get_clicked_pos(mouse_pos)

        if epoch > self.epoch:
            return

        if pygame.mouse.get_pressed()[0]:
            self.grid[epoch][idx].make_alive()
        elif pygame.mouse.get_pressed()[2]:
            self.grid[epoch][idx].make_dead()

    def update(self):
        if self.epoch >= self.max_epochs-1:
            self.start = False
            return

        self.epoch += 1

        new_line = []
        for idx in range(self.line.length):
            new_cell = Cell(self.epoch, idx, width=CELL_WIDTH, height=CELL_HEIGHT)

            cells = (self.line[(idx+i) % self.line.length] for i in range(-1, 2))
            if self.check_rule(cells):
                new_cell.make_alive()
            
            new_line.append(new_cell)
        
        self.line = Line(new_line, self.epoch)
        self.grid.append(self.line)

    def render(self):
        self.screen.fill(GREY)

        for line in self.grid:
            line.render(self.screen)
        
        pygame.display.flip()

    def run(self):
        while self.__runner:
            self.clock.tick(25)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__runner = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.start = not self.start
                    elif event.key == pygame.K_r:
                        self.update()

            self.process_input()
            if self.start:
                self.update()
            self.render()
        
        pygame.quit()


# ElementaryCellularAutomaton(rule=30).run()
