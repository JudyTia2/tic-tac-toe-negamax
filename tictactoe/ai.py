import math
from typing import Optional, Protocol, Tuple

from tictactoe.game import Board, PlayerMark


# ---------- AI ----------
class Strategy(Protocol):
    def best_move(self, board: Board, me: PlayerMark) -> Tuple[int, float]:
        ...


class NegamaxStrategy:
    def evaluate(self, board: Board) -> Optional[int]:
        w = board.winner()
        if w == "X":
            return +1
        if w == "O":
            return -1
        if board.full():
            return 0
        return None

    def negamax(self, board: Board, alpha: float, beta: float, color: int) -> float:
        tv = self.evaluate(board)
        if tv is not None:
            return color * tv
        best = -math.inf
        moves = board.legal_moves()
        mover = board.to_move
        moves.sort(key=lambda i: 0 if board.apply(i).winner() == mover else 1)
        for m in moves:
            val = -self.negamax(board.apply(m), -beta, -alpha, -color)
            best = max(best, val)
            alpha = max(alpha, val)
            if alpha >= beta:
                break
        return best

    def best_move(self, board: Board, me: PlayerMark) -> Tuple[int, float]:
        color = +1 if board.to_move == "X" else -1
        alpha, beta = -math.inf, math.inf
        best_mv, best_val = -1, -math.inf
        for m in board.legal_moves():
            val = -self.negamax(board.apply(m), -beta, -alpha, -color)
            if val > best_val:
                best_val, best_mv = val, m
            alpha = max(alpha, val)
        return best_mv, best_val