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
