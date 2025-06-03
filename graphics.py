from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("root")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()
        print("window closed")
        
    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)



class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Line():
    def __init__(self, point_a, point_b) -> None:
        self.point_a = point_a
        self.point_b = point_b
    
    def draw(self, canvas, fill_color="black"):
        x1, y1 = self.point_a.x, self.point_a.y
        x2, y2 = self.point_b.x, self.point_b.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)
    
