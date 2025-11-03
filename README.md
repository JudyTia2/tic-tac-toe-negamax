# Tic-Tac-Toe with Negamax AI

A classic Tic-Tac-Toe game with a sleek, dark-themed graphical user interface (GUI) built with Python’s native Tkinter library. The application features an unbeatable AI opponent powered by the **Negamax algorithm with alpha-beta pruning**.

## Features

* **Graphical UI:** Responsive, modern Tkinter dark mode.
* **Unbeatable AI:** Perfect play via Negamax + α-β (never loses).
* **Clean Architecture:** Decoupled Game Logic / AI / UI / Players / Controller.
* **Event-Driven:** Smooth user input and game flow.

## Requirements

* **Python 3.9+**
* **Tkinter** (included in the **python.org** installers for Windows/macOS)

  * If you installed Python via Homebrew on macOS and you see `_tkinter` errors, install the python.org build instead (it bundles Tk properly).

## Setup & Installation

This project uses only Python’s standard libraries—no extra packages needed.

1. **Clone the repository**

   ```bash
   git clone https://github.com/JudyTia2/tic-tac-toe-negamax.git
   cd tic_tac_toe
   ```

2. **(Optional) Create a virtual environment**

   ```bash
   # Windows
   python -m venv .venv
   .\.venv\Scripts\activate

   # macOS / Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   > If you have multiple Python versions, you can target 3.9 explicitly:
   > `python3.9 -m venv .venv`

3. **Run the application**

   ```bash
   # Windows
   python main.py

   # macOS / Linux
   python3 main.py
   # (or) python3.9 main.py if you installed 3.9 specifically
   ```

### macOS notes (correct way to run)

* Prefer installing Python 3.9+ from **python.org** (the “macOS 64-bit installer”). This includes Tkinter out of the box.
* If you installed via Homebrew and get `_tkinter` / “No module named _tkinter”:

  * Simplest fix: install Python from **python.org** and run `python3 main.py`.
  * (Alternatively, configure Homebrew’s `python-tk`, which is fussier and varies by version.)

## How to Play

* You play as **X**. The AI plays as **O**.
* Click an empty square to make your move.
* The AI replies automatically after a brief pause.
* Click **Reset** anytime to start a new game.

## Why Negamax + Alpha-Beta?

* **Same theory as Minimax, cleaner code:** Negamax is just Minimax for zero-sum games written in a symmetric form. Instead of separate “Max” and “Min” branches, you use one function and flip the sign when you switch turns. This reduces branching/boilerplate and is easier to maintain.
* **Alpha-beta pruning = big speed-up:** α-β maintains a lower/upper bound (α, β). Any branch that **can’t possibly change the final decision** is cut off early. In Tic-Tac-Toe (max depth 9), this often prunes most of the tree after a strong move is found.
* **Perfect play is feasible:** The state space is tiny; we can search to terminal states (win/draw/loss) with exact scoring. No heuristic needed for 3×3.
* **Move ordering improves pruning:** We try “winning-now” moves first (and blocks next if you add it), which triggers α-β cutoffs earlier and speeds up search.
* **Deterministic & explainable:** Every move is reproducible and traceable; perfect for a take-home where readability and correctness matter.

### Why not alternatives here?

* **Plain Minimax:** Equivalent strength but more verbose (two branches). Negamax is the leaner implementation.
* **Heuristics / depth-limited eval:** Not needed—3×3 can search to the end.

