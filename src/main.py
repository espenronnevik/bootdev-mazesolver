from window import Window
from geometry import Point, Line

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(10, 10), Point(10, 750)), "red")
    win.draw_line(Line(Point(100, 100), Point(200, 200)), "blue")
    win.draw_line(Line(Point(300, 50), Point(500, 500)), "green")
    win.wait_for_close()

if __name__ == "__main__":
    main()
