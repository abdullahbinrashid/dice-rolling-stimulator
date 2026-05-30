import random
import time
import os

# ── pip layouts for each face (3x3 grid positions) ──────────────────────────
# Grid positions:
#  [0][1][2]
#  [3][4][5]
#  [6][7][8]

FACES = {
    1: [4],
    2: [0, 8],
    3: [0, 4, 8],
    4: [0, 2, 6, 8],
    5: [0, 2, 4, 6, 8],
    6: [0, 2, 3, 5, 6, 8],
}

LABELS = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
}

BORDER  = "┌─────────────────────┐"
DIVIDER = "│                     │"
BOTTOM  = "└─────────────────────┘"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def render_face(n):
    pips = FACES[n]
    grid = ["●" if i in pips else " " for i in range(9)]
    rows = [
        f"│   {grid[0]}     {grid[1]}     {grid[2]}   │",
        f"│                     │",
        f"│   {grid[3]}     {grid[4]}     {grid[5]}   │",
        f"│                     │",
        f"│   {grid[6]}     {grid[7]}     {grid[8]}   │",
    ]
    return rows


def draw_die(n, label=""):
    lines = []
    lines.append(BORDER)
    lines.append(DIVIDER)
    for row in render_face(n):
        lines.append(row)
    lines.append(DIVIDER)
    lines.append(BOTTOM)
    if label:
        lines.append(f"         {label}")
    return "\n".join(lines)


def animate_roll():
    frames = 10
    for i in range(frames):
        face = random.randint(1, 6)
        clear()
        print("\n  🎲  DICE ROLLER  🎲\n")
        print(draw_die(face))
        print("\n  Rolling", "." * (i % 4 + 1))
        delay = 0.06 + (i / frames) * 0.1   # slow down toward the end
        time.sleep(delay)


def print_stats(history):
    if not history:
        return
    total = sum(history)
    avg   = total / len(history)
    hi    = max(history)
    lo    = min(history)
    print(f"\n  ─── Stats ───────────────────────────")
    print(f"  Rolls   : {len(history)}")
    print(f"  Total   : {total}")
    print(f"  Average : {avg:.2f}")
    print(f"  High    : {hi}   Low: {lo}")
    recent = history[-8:]
    print(f"  Last    : {' → '.join(str(r) for r in recent)}")
    print(f"  ────────────────────────────────────")


def main():
    history = []

    clear()
    print("\n  🎲  DICE ROLLER  🎲")
    print("  ─────────────────────────────────────")
    print("  Press  ENTER  to roll the die")
    print("  Type   q      then ENTER to quit")
    print("  ─────────────────────────────────────\n")
    print(draw_die(6, "Ready!"))

    while True:
        try:
            key = input("\n  > ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            break

        if key in ("q", "quit", "exit"):
            clear()
            print("\n  Thanks for playing! Final stats:")
            print_stats(history)
            print("\n  Goodbye 👋\n")
            break

        # Any key (including just Enter) rolls the die
        animate_roll()
        result = random.randint(1, 6)
        history.append(result)

        clear()
        print("\n  🎲  DICE ROLLER  🎲\n")
        print(draw_die(result, f"Rolled: {result}  ({LABELS[result]})"))
        print_stats(history)
        print("\n  Press ENTER to roll again  |  q + ENTER to quit")


if __name__ == "__main__":
    main()