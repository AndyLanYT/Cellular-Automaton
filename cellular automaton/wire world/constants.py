WIDTH = 800
HEIGHT = 800

ROWS = 40
COLS = 35

CELL_WIDTH = CELL_HEIGHT = min(WIDTH // COLS, HEIGHT // ROWS)

GRID_WIDTH = CELL_WIDTH * COLS
GRID_HEIGHT = CELL_HEIGHT * ROWS

WIDTH = GRID_WIDTH
HEIGHT = GRID_HEIGHT

UP = 0, -1
DOWN = 0, 1
LEFT = -1, 0
RIGHT = 1, 0
UP_LEFT = -1, -1
UP_RIGHT = 1, -1
DOWN_LEFT = -1, 1
DOWN_RIGHT = 1, 1

MOORE_NEIGHBORHOOD = [UP, DOWN, LEFT, RIGHT, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT]
VON_NEUMANN_NEIGHBORHOOD = [UP, DOWN, LEFT, RIGHT]
