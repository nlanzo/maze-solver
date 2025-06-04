from graphics import Line, Point

class Cell():
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self.__win is None:
            return
        if x2 >= x1:
            self.__x1 = x1
            self.__x2 = x2
        else:
            self.__x1 = x2
            self.__x2 = x1
        if y2 >= y1:
            self.__y1 = y1
            self.__y2 = y2
        else:
            self.__y1 = y2
            self.__y2 = y1

        
        left_wall = Line(Point(x1, y1), Point(x1, y2))
        if self.has_left_wall:
            self.__win.draw_line(left_wall)
        else:
            self.__win.draw_line(left_wall, "white")
            
        top_wall = Line(Point(x1, y1), Point(x2, y1))
        if self.has_top_wall:
            self.__win.draw_line(top_wall)
        else:
            self.__win.draw_line(top_wall, "white")

        right_wall = Line(Point(x2, y1), Point(x2, y2))
        if self.has_right_wall:
            self.__win.draw_line(right_wall)
        else:
            self.__win.draw_line(right_wall, "white")

        bottom_wall = Line(Point(x1, y2), Point(x2, y2))
        if self.has_bottom_wall:
            self.__win.draw_line(bottom_wall)
        else:
            self.__win.draw_line(bottom_wall, "white")


    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        from_x, from_y = self.get_midpoint()
        to_x, to_y = to_cell.get_midpoint()
        point_from = Point(from_x, from_y)
        point_to = Point(to_x, to_y)
        self.__win.draw_line(Line(point_from, point_to), color)


    def get_midpoint(self):
        mid_x = (self.__x2 + self.__x1) // 2
        mid_y = (self.__y2 + self.__y1) // 2
        return mid_x, mid_y