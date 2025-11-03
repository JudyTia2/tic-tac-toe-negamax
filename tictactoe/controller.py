from __future__ import annotations
from typing import Dict

from tictactoe.game import Board, PlayerMark
from tictactoe.players import ComputerPlayer, HumanPlayer, Player
from tictactoe.ui import DarkTkApp


class GameController:
    def __init__(self, players: Dict[PlayerMark, Player], ui: DarkTkApp):
        self.players = players
        self.ui = ui
        self.board = Board.new()

    def start(self) -> None:
        self.ui.render(self.board)
        self.play_turn()

    def play_turn(self) -> None:
        if self.board.terminal():
            return

        player = self.players[self.board.to_move]
        if isinstance(player, HumanPlayer):
            # For a human, do nothing. The UI will call handle_move on click.
            pass
        elif isinstance(player, ComputerPlayer):
            # For a computer, schedule the AI's move.
            self.ui.root.after(200, self.ai_move)

    def handle_move(self, move: int) -> None:
        if move not in self.board.legal_moves():
            return
        self.board = self.board.apply(move)
        self.ui.render(self.board)
        self.play_turn()

    def ai_move(self) -> None:
        player = self.players[self.board.to_move]
        move = player.move(self.board)
        self.handle_move(move)

    def reset(self) -> None:
        self.board = Board.new()
        self.ui.render(self.board)
        self.play_turn()