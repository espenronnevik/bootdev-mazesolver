class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

class Cell(object):
    def __init__(self, topleft_x, topleft_y, bottomright_x, bottomright_y, window):
        self._window = window

        self._topleft = Point(topleft_x, topleft_y)
        self._bottomleft = Point(topleft_x, bottomright_y)
        self._topright = Point(bottomright_x, topleft_y)
        self._bottomright = Point(bottomright_x, bottomright_y)

        med_x = (topleft_x + bottomright_x) // 2
        med_y = (topleft_y + bottomright_y) // 2
        self.center = Point(med_x, med_y)

        self._top = Line(self._topleft, self._topright)
        self._left = Line(self._topleft, self._bottomleft)
        self._right = Line(self._topright, self._bottomright)
        self._bottom = Line(self._bottomleft, self._bottomright)

        self.has_top = True
        self.has_left = True
        self.has_right = True
        self.has_bottom = True

    def draw(self, fill_color):
        if self.has_top:
            self._window.draw_line(self._top, fill_color)
        if self.has_left:
            self._window.draw_line(self._left, fill_color)
        if self.has_right:
            self._window.draw_line(self._right, fill_color)
        if self.has_bottom:
            self._window.draw_line(self._bottom, fill_color)

    def draw_move(self, to_cell, undo=False):
        centerline = Line(self.center, to_cell.center)
        if undo:
            self._window.draw_line(centerline, "gray")
        else:
            self._window.draw_line(centerline, "red")
