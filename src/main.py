from window import Window
from geometry import Point, Line, Cell

def main():
    win = Window(800, 800)
    c1 = Cell(10, 100, 110, 200, win)
    c1.has_bottom = False
    c1.draw("black")
    c2 = Cell(115, 100, 215, 200, win)
    c2.has_left = False
    c2.has_right = False
    c2.draw("red")
    c3 = Cell(220, 100, 320 , 200, win)
    c3.has_top = False
    c3.has_right = False
    c3.draw("blue")
    win.wait_for_close()

if __name__ == "__main__":
    main()
