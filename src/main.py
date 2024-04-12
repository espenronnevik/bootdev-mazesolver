from window import Window
from geometry import Point, Line, Cell

def main():
    win = Window(800, 800)
    c1 = Cell(10, 10, 210, 210, win)
    c1.has_right = False
    c1.draw("black")
    c2 = Cell(210, 10, 420, 210, win)
    c2.has_left = False
    c2.has_right = False
    c2.draw("red")
    c3 = Cell(410, 10, 630, 210, win)
    c3.has_left = False
    c3.draw("blue")
    c1.draw_move(c2)
    c2.draw_move(c3, undo=True)

    win.wait_for_close()

if __name__ == "__main__":
    main()
