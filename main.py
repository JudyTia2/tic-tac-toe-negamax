from __future__ import annotations
import tkinter as tk
from typing import Dict

from tictactoe.ai import NegamaxStrategy
from tictactoe.controller import GameController
from tictactoe.game import PlayerMark
from tictactoe.players import ComputerPlayer, HumanPlayer, Player
from tictactoe.ui import DarkTkApp


if __name__ == "__main__":
    root = tk.Tk()
    players: Dict[PlayerMark, Player] = {
        "X": HumanPlayer("X"),
        "O": ComputerPlayer("O", NegamaxStrategy()),
    }
    app = DarkTkApp(root, on_move=lambda m: controller.handle_move(m), on_reset=lambda: controller.reset())
    app.set_human_player("X")
    controller = GameController(players, app)
    controller.start()
    app.run_forever()
