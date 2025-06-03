from cell import Cell
from time import sleep


class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__window = window
        self.__cells = []

        self.__create_cells()



    def __create_cells(self):
        for i in range(self.__num_cols):
            row = []
            for j in range(self.__num_rows):
                row.append(Cell(self.__window))
            self.__cells.append(row)

        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        cell = self.__cells[i][j]
        x1 = self.__x1 + self.__cell_size_x * i
        y1 = self.__y1 + self.__cell_size_y * j
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y

        cell.draw(x1, y1, x2, y2)

        self.__animate()
    
    def __animate(self):
        if self.__window is None:
            return
        self.__window.redraw()
        sleep(0.05)