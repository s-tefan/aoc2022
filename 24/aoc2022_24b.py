def move(blizzard, n_rows, n_cols):
    (row, col), dir = blizzard
    match dir:
        case "v":
            row = (row + 1) % n_rows
        case "^":
            row = (row - 1) % n_rows
        case ">":
            col = (col + 1) % n_cols
        case "<":
            col = (col - 1) % n_cols
    return ((row, col), dir)


def moved(blizzards, n_rows, n_cols):
    return {move(blizzard, n_rows, n_cols) for blizzard in blizzards}


def print_diagram():
    for r in range(n_maprows):
        symbolrow = ""
        for c in range(n_mapcols):
            symbol, n = ".", 0
            if (r, c) == pos:
                symbol = "E"
            for k in "<>v^":
                if ((r, c), k) in blizzards:
                    symbol = k
                    n += 1
            if n > 1:
                symbol = str(n)
            symbolrow += symbol
        print(symbolrow)


def part(n_part):
    global blizzards
    finished, back, second = False, False, False
    pos_set = {(-1, 0, False, False)}
    # Do a breadth first traversal, until reaching finish
    k = 0
    while not finished:
        k += 1
        blizzards = moved(blizzards, n_maprows, n_mapcols)
        blizzard_pos = {blizz[0] for blizz in blizzards}
        new_pos_set = set()
        for pos in pos_set:
            r, c, back, second = pos
            for r, c in (
                (r, c),
                ((r + 1), c),
                ((r - 1), c),
                (r, (c - 1)),
                (r, (c + 1)),
            ):

                if (
                    (0 <= r < n_maprows and 0 <= c < n_mapcols)
                    or (r, c) == (-1, 0)
                    or (r, c) == (n_maprows, n_mapcols - 1)
                ):
                    if (r, c) not in blizzard_pos:
                        this_back, this_second = back, second
                        if r == n_maprows and c == n_mapcols - 1:
                            if n_part == 1:
                                finished = True
                                print(f"Finish reached after {k} steps")
                                break
                            elif n_part == 2:
                                if second:
                                    finished = True
                                    print(f"Finish reached after {k} steps")
                                    break
                                else:
                                    this_back = True
                        if back and (r, c) == (-1, 0):
                            this_second = True
                        new_pos_set.add((r, c, this_back, this_second))
        pos_set = new_pos_set


filename = "input.txt"

with open(filename) as f:
    lines = f.readlines()
map = [line.strip()[1:-1] for line in lines[1:-1]]
blizzards = set()
for rownr, row in enumerate(map):
    for colnr, c in enumerate(row):
        if c in "<>v^":
            blizzards.add(((rownr, colnr), c))

n_maprows, n_mapcols = len(map), len(map[0])

blizzards_original = blizzards.copy()

part(1)
blizzards = blizzards_original.copy()
part(2)
