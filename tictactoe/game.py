"""
This module contains the core game logic and state representation for Tic-Tac-Toe.
It defines the game board, rules for making moves, and conditions for winning or drawing.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import List, Literal, Optional

Mark = Literal["X", "O", " "]
PlayerMark = Literal["X", "O"]

# ---------- Model ----------
WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


@dataclass
class Board:
    cells: List[Mark]
    to_move: PlayerMark

    @staticmethod
    def new() -> "Board":
        return Board([" "] * 9, "X")

    def copy(self) -> "Board":
        return Board(self.cells[:], self.to_move)

    def legal_moves(self) -> List[int]:
        return [i for i, c in enumerate(self.cells) if c == " "]

    def apply(self, idx: int) -> "Board":
        if self.cells[idx] != " ":
            raise ValueError(f"Cell {idx} is already occupied")
        b = self.copy()
        b.cells[idx] = b.to_move
        b.to_move = "O" if b.to_move == "X" else "X"
        return b

    def winner(self) -> Optional[PlayerMark]:
        for a, b, c in WIN_LINES:
            line = self.cells[a] + self.cells[b] + self.cells[c]
            if line == "XXX":
                return "X"
            if line == "OOO":
                return "O"
        return None

    def full(self) -> bool:
        return all(c != " " for c in self.cells)

    def terminal(self) -> bool:
        return self.winner() is not None or self.full()