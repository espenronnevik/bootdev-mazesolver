import random
from time import sleep

from geometry import Cell

class Maze(object):
    def __init__(self, x1, y1, num_cols, num_rows, cell_size_x, cell_size_y, window=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_cols = num_cols
        self._num_rows = num_rows
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window

        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            self._cells.append([])
            y1 = self._y1 + (self._cell_size_y * i)
            y2 = y1 + self._cell_size_y
            for j in range(self._num_rows):
                x1 = self._x1 + (self._cell_size_x * j)
                x2 = x1 + self._cell_size_x
                cell = Cell(x1, y1, x2, y2, self._window)
                self._cells[i].append(cell)
                cell.draw("black")

    def _draw_cells(self, *cells):
        if self._window:
            for cell in cells:
                cell.draw("black")
                self._animate()

    def _animate(self):
        if self._window:
            self._window.redraw()
            sleep(0.05)

    def _break_entrance_and_exit(self):
        begincell = self._cells[0][0]
        begincell.has_left = False
        begincell.draw("black")
        endcell = self._cells[-1][-1]
        endcell.has_right = False
        endcell.draw("black")

    def _valid_cell(self, col, row):
        if col < 0 or col >= self._num_cols or row < 0 or row >= self._num_rows:
            return None
        return self._cells[col][row]

    def _break_walls_r(self, col, row):
        currentcell = self._cells[col][row]
        currentcell.visited = True

        # Return early if we have broken into the "exit" cell
        if currentcell == self._cells[-1][-1]:
            self._draw_cells(currentcell)
            return

        valid_moves = {"up": [col - 1, row], "down": [col + 1, row], "right": [col, row + 1], "left": [col, row - 1]}
        while True:
            possible_moves = {}

            for k, v in valid_moves.items():
                cell = self._valid_cell(v[0], v[1])
                if cell is not None and not cell.visited:
                    possible_moves[k] = cell

            if len(possible_moves) == 0:
                self._draw_cells(currentcell)
                return

            rdirection = random.choice(list(possible_moves.keys()))
            nextcell = possible_moves[rdirection]
            if rdirection == "up":
                currentcell.has_top = False
                nextcell.has_bottom = False
            elif rdirection == "right":
                currentcell.has_right = False
                nextcell.has_left = False
            elif rdirection == "down":
                currentcell.has_bottom = False
                nextcell.has_top = False
            elif rdirection == "left":
                currentcell.has_left = False
                nextcell.has_right = False

            self._draw_cells(currentcell, nextcell)
            self._break_walls_r(valid_moves[rdirection][0], valid_moves[rdirection][1])
