from maze import Maze
from window import Window


def main():
    offset_x = 5
    offset_y = 5
    num_cols = 20
    num_rows = 40
    cellsize_x = 30
    cellsize_y = 30

    winsize_x = (offset_x * 2) + (num_rows * cellsize_x)
    winsize_y = (offset_y * 2) + (num_cols * cellsize_y)

    win = Window(winsize_x, winsize_y)
    maze = Maze(offset_x, offset_y, num_cols, num_rows, cellsize_x, cellsize_y, win)
    maze.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()
