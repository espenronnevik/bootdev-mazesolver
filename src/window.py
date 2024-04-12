from tkinter import Tk, BOTH, Canvas

class Window(object):
        def __init__(self, height, width):
            self._root = Tk()
            self._root.title("Maze Solver")
            self._root.protocol("WM_DELETE_WINDOW", self.close)
            self._canvas = Canvas(self._root, height=height, width=width)
            self._canvas.pack()
            self._running = False

        def redraw(self):
            self._root.update_idletasks()
            self._root.update()

        def wait_for_close(self):
            self._running = True
            while self._running:
                self.redraw()

        def close(self):
            self._running = False
