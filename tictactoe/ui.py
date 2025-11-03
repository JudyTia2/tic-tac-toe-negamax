import tkinter as tk
from typing import Callable, Dict, Optional

from tictactoe.game import Board, PlayerMark


class DarkTkApp:
    def __init__(self, root: tk.Tk, on_move: Callable[[int], None], on_reset: Callable[[], None]):
        self.root = root
        self.on_move = on_move
        self.on_reset = on_reset

        self.root.title("Tic-Tac-Toe ✕ Negamax")
        self.root.configure(bg="#121212")

        self.buttons: list[tk.Button] = []
        self.human_player_mark: Optional[PlayerMark] = None

        self.status = tk.Label(
            self.root, text="Starting...",
            font=("Segoe UI", 14, "bold"),
            fg="#FFFFFF", bg="#121212"
        )
        self.status.grid(row=0, column=0, columnspan=3, pady=(8, 4))

        for r in range(3):
            for c in range(3):
                idx = r * 3 + c
                btn = tk.Button(
                    self.root, text=" ", width=4, height=2,
                    font=("Segoe UI", 36, "bold"),
                    fg="#FFFFFF", bg="#1E1E1E",
                    activebackground="#2C2C2C", activeforeground="#00FFB7",
                    relief="flat", bd=0,
                    command=lambda i=idx: self.on_click(i)
                )
                btn.grid(row=r+1, column=c, padx=6, pady=6, sticky="nsew")
                self.buttons.append(btn)

        self.reset_btn = tk.Button(
            self.root, text="Reset", command=self.on_reset,
            font=("Segoe UI", 12, "bold"),
            fg="#FFFFFF", bg="#121212",
            activebackground="#2C2C2C", activeforeground="#FFFFFF",
            relief="solid", bd=1, highlightbackground="#FFFFFF", highlightcolor="#FFFFFF",
            width=8
        )
        self.reset_btn.grid(row=4, column=0, columnspan=3, pady=(10, 12))

        for i in range(3):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(1, 4):
            self.root.grid_rowconfigure(i, weight=1)

    def set_human_player(self, mark: PlayerMark) -> None:
        """Set which mark the human player is controlling."""
        self.human_player_mark = mark

    def render(self, board: Board) -> None:
        """Render the board state and status message."""
        for i, btn in enumerate(self.buttons):
            mark = board.cells[i]
            btn.config(text=mark)
            if mark == "X":
                btn.config(fg="#00BFFF")
            elif mark == "O":
                btn.config(fg="#FF4B4B")

            # A button is clickable if the cell is empty, the game is not over,
            # and it's the human player's turn.
            is_human_turn = (board.to_move == self.human_player_mark)
            clickable = (mark == " " and not board.terminal() and is_human_turn)
            btn.config(state=("normal" if clickable else "disabled"))

        if board.terminal():
            w = board.winner()
            msg = "Draw." if w is None else f"{w} wins!"
            self.status.config(text=msg, fg="#FFFFFF")
        else:
            msg = f"{board.to_move} to move"
            if board.to_move != self.human_player_mark:
                msg += " (AI thinking...)"
            self.status.config(text=msg, fg="#FFFFFF")

        self.root.update_idletasks()

    def on_click(self, idx: int) -> None:
        """Handle a human player's click on a board button."""
        self.on_move(idx)

    def run_forever(self) -> None:
        """Start the Tkinter main loop."""
        self.root.mainloop()