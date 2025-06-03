from graphics import Line, Point

class Cell():
    def __init__(self, window) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        if self.has_left_wall:
            left_wall = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(left_wall)
        if self.has_top_wall:
            top_wall = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(top_wall)
        if self.has_right_wall:
            right_wall = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(right_wall)
        if self.has_bottom_wall:
            bottom_wall = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(bottom_wall)
