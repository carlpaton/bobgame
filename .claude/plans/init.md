# Bobgame – Milestone 1 Plan

## Context
Bobgame is a top-down shooter in Python, run as a local desktop app (not in a browser). It must run on Ubuntu first, and the library must also support Windows for later. The repo is currently empty apart from README.md and prompt.txt.

Milestone 1 goals (from prompt.txt):
- A blank window showing the round top of a man's head (Bob).
- Bob moves with WASD.
- Bob has an arrow showing his front.

## Decisions (from clarifying questions)
- Language: **Python 3 only** (Python 2 is end-of-life and pygame no longer supports it). Target **Python 3.10+**, which is the version Ubuntu 22.04 ships, and it also runs on Windows. Use `python3` on Ubuntu and `py -3` on Windows. Declare the minimum in the README, and use type hints and `pathlib` where useful.
- Library: **pygame** (cross-platform: Ubuntu now, Windows later).
- Facing: **mouse aim**. The arrow points at the cursor and WASD only moves Bob.
- Graphics: **code-drawn shapes**, no asset files.
- Window: **800x600**, Bob clamped inside the window, frame-rate-independent speed.

## Project layout
```
bobgame/
  requirements.txt     # pygame
  main.py              # entry point: python main.py
  bobgame/
    __init__.py
    settings.py        # WIDTH, HEIGHT, FPS, BG colour, BOB_SPEED, BOB_RADIUS
    player.py          # Bob: position, update(dt, keys, mouse_pos), draw(surface)
    game.py            # Game class: window, event loop, update/draw
  README.md            # setup + run instructions (Ubuntu venv, Windows note)
```

## Implementation steps
1. `requirements.txt` with `pygame`; check `python3 --version` is 3.10 or newer, create a venv (`python3 -m venv .venv`) and install. If `venv` is missing on Ubuntu, run `sudo apt install python3-venv`.
2. `settings.py`: constants (800x600, 60 FPS, dark background, Bob radius ~20, speed ~250 px/s).
3. `player.py` – `Bob` class:
   - `pos` as `pygame.Vector2`, starting at the window centre.
   - `update(dt, keys, mouse_pos)`:
     - Build a direction vector from W/A/S/D (W = up, S = down, A = left, D = right).
     - Normalise it so diagonals aren't faster.
     - `pos += dir * speed * dt`.
     - Clamp `pos` to `[radius, WIDTH - radius]` and `[radius, HEIGHT - radius]`.
     - Compute `facing = (mouse_pos - pos).normalize()`, skipping this if the distance is zero.
   - `draw(surface)`:
     - Head circle in skin tone, with a hair-coloured cap or ring so it reads as the top of a man's head.
     - Arrow from the head centre outward along `facing`: a line plus a triangle tip, extending a little beyond the head radius.
4. `game.py` – `Game` class:
   - `pygame.init()`, create the window, set the caption "Bobgame", and make a `Clock`.
   - Loop: `dt = clock.tick(FPS) / 1000`, handle `QUIT` and `Esc`, call `bob.update(...)`, fill the background, call `bob.draw(...)`, then `display.flip()`.
5. `main.py`: `from bobgame.game import Game; Game().run()`.
6. README: Ubuntu setup and run commands. Note that Windows works with the same code (`py -m venv`, `pip install -r requirements.txt`).

## Verification
- `python3 --version` reports 3.10 or newer inside the venv.
- `python3 main.py` opens an 800x600 window with Bob in the centre.
- W/A/S/D move Bob up/left/down/right. Diagonal speed matches straight-line speed. Bob stops at all four edges.
- The arrow follows the mouse cursor from any position, with no errors when the cursor is over Bob's centre.
- Closing the window or pressing Esc exits cleanly.
- Optional: a headless smoke test with `SDL_VIDEODRIVER=dummy` that runs a few frames of `Game` and checks `Bob.update` clamping and normalisation.

## Out of scope (later milestones)
Shooting, enemies, collision, sprites and art, sound, menus.
