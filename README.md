# bobgame

A top-down shooter in Python (pygame-ce, same `import pygame`), run as a local desktop app.
Milestone 1: Bob moves with WASD and an arrow points at the mouse cursor.

Requires Python 3.10+.

## Ubuntu
```
sudo apt install python3-venv   # if venv is missing
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python main.py
```

## Windows
```
py -3 -m venv .venv
.venv\Scripts\pip install -r requirements.txt
.venv\Scripts\python main.py
```

Controls: W/A/S/D move, mouse aims, Esc quits.
