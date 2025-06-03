from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell2 = Cell(win)
    cell1.draw(50, 50, 150, 150)
    cell2.draw(500, 500, 400, 400)
    win.wait_for_close()


main()