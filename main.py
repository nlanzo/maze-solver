from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell2 = Cell(win)
    cell3 = Cell(win)
    cell1.has_bottom_wall = False
    cell2.has_top_wall = False
    cell3.has_right_wall = False
    cell3.has_left_wall = False
    cell1.draw(50, 50, 150, 150)
    cell2.draw(50, 200, 250, 250)
    cell3.draw(390, 390, 300, 300)
    cell1.draw_move(cell2)
    cell2.draw_move(cell3, undo=True)
    win.wait_for_close()


main()