import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_cell_count(self):
        num_cols = 7
        num_rows = 13
        count = 0
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        for i in range(num_cols):
            count += len(m1._cells[i])
        self.assertEqual(num_cols * num_rows, count)

    def test_reset_visited(self):
        num_cols = 3
        num_rows = 2
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        m1._reset_cells_visited()
        for col in m1._cells:
            for cell in col:
                self.assertEqual(cell.visited, False)
