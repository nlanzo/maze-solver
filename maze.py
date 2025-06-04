from cell import Cell
from time import sleep
import random


class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None, seed=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__window = window
        self.__cells = []
        if seed:
            self.__seed = random.seed(seed)

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)




    def __create_cells(self):
        for i in range(self.__num_cols):
            column = []
            for j in range(self.__num_rows):
                column.append(Cell(self.__window))
            self.__cells.append(column)

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
        sleep(0.02)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            to_visit = []
            # check right
            if i < self.__num_cols - 1 and not self.__cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            # check down
            if j < self.__num_rows - 1 and not self.__cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
            # check left
            if i > 0 and not self.__cells[i - 1][j].visited: 
                to_visit.append((i - 1, j))
            # check up
            if j > 0 and not self.__cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            
            if len(to_visit) == 0:
                self.__draw_cell(i, j)
                return
            
            direction_index = random.randrange(len(to_visit))
            next_to_visit = to_visit[direction_index]

            # go right
            if next_to_visit[0] == i + 1:
                self.__cells[i][j].has_right_wall = False
                self.__cells[i + 1][j].has_left_wall = False
            # go down
            if next_to_visit[1] == j + 1:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][j + 1].has_top_wall = False
            # go left
            if next_to_visit[0] == i - 1:
                self.__cells[i][j].has_left_wall = False
                self.__cells[i - 1][j].has_right_wall = False
            # go up
            if next_to_visit[1] == j - 1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][j - 1].has_bottom_wall = False


            self.__break_walls_r(next_to_visit[0], next_to_visit[1])
            