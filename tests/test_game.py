import unittest
from typing import List

from tictactoe.game import Board, Mark, WIN_LINES


class TestBoard(unittest.TestCase):
    def test_new_board_is_empty(self):
        board = Board.new()
        self.assertEqual(board.cells, [" "] * 9)
        self.assertEqual(board.to_move, "X")

    def test_apply_move_is_immutable(self):
        board1 = Board.new()
        board2 = board1.apply(0)
        self.assertNotEqual(board1, board2, "apply() should return a new board object")
        self.assertEqual(board1.cells[0], " ", "Original board should not be modified")

    def test_apply_move_updates_state(self):
        board = Board.new()
        board = board.apply(4)  # X moves to center
        self.assertEqual(board.cells[4], "X")
        self.assertEqual(board.to_move, "O")

        board = board.apply(0)  # O moves to top-left
        self.assertEqual(board.cells[0], "O")
        self.assertEqual(board.to_move, "X")

    def test_legal_moves(self):
        board = Board.new()
        self.assertEqual(board.legal_moves(), list(range(9)))

        board = board.apply(0).apply(1).apply(2)
        self.assertEqual(board.legal_moves(), [3, 4, 5, 6, 7, 8])

        full_board_cells: List[Mark] = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]
        full_board = Board(full_board_cells, "X")
        self.assertEqual(full_board.legal_moves(), [])

    def test_winner(self):
        for player in ("X", "O"):
            for line in WIN_LINES:
                with self.subTest(player=player, line=line):
                    cells: List[Mark] = [" "] * 9
                    for pos in line:
                        cells[pos] = player
                    board = Board(cells, "X" if player == "O" else "O")
                    self.assertEqual(board.winner(), player)

    def test_draw_condition(self):
        draw_cells: List[Mark] = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]
        draw_board = Board(draw_cells, "X")
        self.assertIsNone(draw_board.winner())
        self.assertTrue(draw_board.full())
        self.assertTrue(draw_board.terminal())

    def test_apply_invalid_move_raises_error(self):
        board = Board.new().apply(0)  # X plays at 0
        # O tries to play at 0 again
        with self.assertRaises(ValueError):
            board.apply(0)

    def test_full_board(self):
        board = Board.new()
        self.assertFalse(board.full())

        full_board_cells: List[Mark] = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]
        full_board = Board(full_board_cells, "X")
        self.assertTrue(full_board.full())

    def test_terminal_state(self):
        # Game not over
        board = Board.new()
        self.assertFalse(board.terminal())

        # Game over by win
        win_cells: List[Mark] = ["X", "X", "X", "O", "O", " ", " ", " ", " "]
        win_board = Board(win_cells, "O")
        self.assertTrue(win_board.terminal())

        # Game over by draw
        draw_cells: List[Mark] = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]
        draw_board = Board(draw_cells, "X")
        self.assertTrue(draw_board.terminal())
