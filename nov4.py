import os
import time

width = 20
height = 10
generation = 25

initial = [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)]


def create_grid():
    grid = [[0] * width for _ in range(height)]
    for r, c in initial:
        grid[r][c] = 1
    return grid


def print_grid(g):
    os.system("cls" if os.name == "nt" else "clear")
    display = ["".join("#" if cell else "." for cell in row) for row in g]
    print("\n".join(display))
    print("-" * width)


def count_neighbors(g, r, c):
    return sum(
        g[r + dr][c + dc] == 1
        for dr in [-1, 0, 1]
        for dc in [-1, 0, 1]
        if not (dr == 0 and dc == 0)
        and 0 <= r + dr < height
        and 0 <= c + dc < width
    )


def update_grid(g):
    new_g = [[0] * width for _ in range(height)]
    for r in range(height):
        for c in range(width):
            neighbors = count_neighbors(g, r, c)
            is_alive = g[r][c] == 1

            if is_alive and neighbors in [2, 3]:
                new_g[r][c] = 1
            elif not is_alive and neighbors == 3:
                new_g[r][c] = 1
    return new_g


def run_simulation():
    grid = create_grid()
    for gen in range(generation):
        print_grid(grid)
        print(f"generation: {gen + 1}")
        grid = update_grid(grid)
        time.sleep(0.3)


run_simulation()