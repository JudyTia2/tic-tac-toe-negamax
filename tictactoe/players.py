from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol

from tictactoe.ai import Strategy
from tictactoe.game import Board, PlayerMark


class Player(Protocol):
    mark: PlayerMark
    def move(self, board: Board) -> int: ...


@dataclass
class HumanPlayer(Player):
    mark: PlayerMark
    def move(self, board: Board) -> int:
        raise NotImplementedError("Human move is handled by the UI.")


@dataclass
class ComputerPlayer(Player):
    mark: PlayerMark
    strategy: Strategy
    def move(self, board: Board) -> int:
        mv, _ = self.strategy.best_move(board, self.mark)
        return mv