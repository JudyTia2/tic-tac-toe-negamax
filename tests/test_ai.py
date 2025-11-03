import unittest

from tictactoe.ai import NegamaxStrategy
from tictactoe.game import Board


class TestNegamaxStrategy(unittest.TestCase):
    def setUp(self):
        self.strategy = NegamaxStrategy()

    def test_evaluate_terminal_states(self):
        # X wins
        board_x_wins = Board(["X", "X", "X", "O", "O", " ", " ", " ", " "], "O")
        self.assertEqual(self.strategy.evaluate(board_x_wins), 1)

        # O wins
        board_o_wins = Board(["O", "O", "O", "X", "X", " ", "X", " ", " "], "X")
        self.assertEqual(self.strategy.evaluate(board_o_wins), -1)

        # Draw
        draw_board = Board(["X", "O", "X", "O", "X", "O", "O", "X", "O"], "X")
        self.assertEqual(self.strategy.evaluate(draw_board), 0)

        # Non-terminal
        ongoing_board = Board.new()
        self.assertIsNone(self.strategy.evaluate(ongoing_board))

    def test_ai_makes_winning_move(self):
        # AI is 'O' and can win at index 5
        board = Board(["X", "X", " ", "O", "O", " ", "X", " ", " "], "O")
        best_move, _ = self.strategy.best_move(board, "O")
        self.assertEqual(best_move, 5)

    def test_ai_blocks_opponent_win(self):
        # AI is 'O' and must block X at index 2
        board = Board(["X", "X", " ", "O", " ", " ", " ", " ", " "], "O")
        best_move, _ = self.strategy.best_move(board, "O")
        self.assertEqual(best_move, 2)

    def test_ai_chooses_optimal_opening_move(self):
        # AI is 'X' (going first)
        board = Board.new()
        best_move, _ = self.strategy.best_move(board, "X")
        # A perfect player will always start in the center or a corner.
        optimal_openings = {0, 2, 4, 6, 8}
        self.assertIn(best_move, optimal_openings)
