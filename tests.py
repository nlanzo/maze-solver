import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_create_cells_dimension_valid(self):
        num_cols = 14
        num_rows = 11
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m2._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m2._Maze__cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 14
        num_rows = 11
        m3 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m3._Maze__break_entrance_and_exit()
        self.assertEqual(
            m3._Maze__cells[0][0].has_left_wall,
            True,
        )
        self.assertEqual(
            m3._Maze__cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m3._Maze__cells[num_cols - 1][num_rows - 1].has_right_wall,
            True,
        )
        self.assertEqual(
            m3._Maze__cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

    def test_reset_cells_visited(self):
        num_cols = 14
        num_rows = 11
        m4 = Maze(0, 0, num_rows, num_cols, 10, 10, None, 10)
        m4._Maze__break_entrance_and_exit()
        m4._Maze__break_walls_r(0, 0)
        m4._Maze__reset_cells_visited()
        cell_status = []
        for col in m4._Maze__cells:
            for cell in col:
                cell_status.append(cell.visited)
        self.assertEqual(
            cell_status,
            [False for i in range(num_cols * num_rows)]
        )


if __name__ == "__main__":
    unittest.main()