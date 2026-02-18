import time
import os

# ======================
# ===== ADT ARRAY2D ====
# ======================

class Array2D:
    def __init__(self, rows, cols):
        self.rowEff = rows
        self.colEff = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def get(self, i, j):
        return self.data[i][j]

    def set(self, i, j, value):
        self.data[i][j] = value

    def print_array(self):
        for i in range(self.rowEff):
            for j in range(self.colEff):
                if self.data[i][j] == 1:
                    print("■", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()


# ==========================
# ===== GAME OF LIFE =======
# ==========================

def count_neighbors(arr, row, col):
    count = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            r = row + i
            c = col + j

            if (0 <= r < arr.rowEff and
                0 <= c < arr.colEff and
                not (i == 0 and j == 0)):
                count += arr.get(r, c)

    return count


def next_generation(arr):
    temp = Array2D(arr.rowEff, arr.colEff)

    for i in range(arr.rowEff):
        for j in range(arr.colEff):
            neighbors = count_neighbors(arr, i, j)

            if arr.get(i, j) == 1:
                if neighbors < 2 or neighbors > 3:
                    temp.set(i, j, 0)
                else:
                    temp.set(i, j, 1)
            else:
                if neighbors == 3:
                    temp.set(i, j, 1)
                else:
                    temp.set(i, j, 0)

    return temp


# ======================
# ======= MAIN =========
# ======================

def main():
    rows, cols = 10, 10
    grid = Array2D(rows, cols)

    # Pola awal (Glider)
    grid.set(1, 2, 1)
    grid.set(2, 3, 1)
    grid.set(3, 1, 1)
    grid.set(3, 2, 1)
    grid.set(3, 3, 1)

    generations = 20

    for gen in range(generations):
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Generasi {gen}")
        grid.print_array()
        time.sleep(0.5)
        grid = next_generation(grid)


if __name__ == "__main__":
    main()