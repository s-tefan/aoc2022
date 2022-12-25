filename = "input.txt"
with open(filename) as f:
    lines = f.readlines()
map = []
line_iter = iter(lines)
while line := next(line_iter):
    if line.strip():
        start = 0
        row = ""
        for k, c in enumerate(line):
            if c == " ":
                start += 1
            elif c == "\n":
                break
            else:
                row = row + c
        map.append((row, start))
    else:
        break
path = next(line_iter)


class Path:
    def __init__(self, string):
        self.string = string

    def __iter__(self):
        return self

    def __next__(self):
        if self.string:
            s = ""
            while self.string and self.string[0] not in {"R", "L"}:
                s = s + self.string[0]
                self.string = self.string[1:]
            if s:
                return int(s)
            elif self.string:
                s = self.string[0]
                self.string = self.string[1:]
                return s
            else:
                raise StopIteration
        else:
            raise StopIteration


def turn(dir, turncode):
    dr, dc = dir  # dr south, dc east
    if turncode == "L":
        return -dc, dr
    elif turncode == "R":
        return dc, -dr
    else:
        raise Exception("Wrong turncode")


def get(map, pos):
    maprow, rowstart = map[pos[0]]
    print(pos)
    return maprow[pos[1] - rowstart]


def nextstep(pos, dir, map):
    if dir[1] == 0:
        newposcol = pos[1]
        newposrow = pos[0] + dir[0]
        if (
            newposrow < 0
            or newposrow >= len(map)
            or newposcol < map[newposrow][1]
            or newposcol >= map[newposrow][1] + len(map[newposrow][0])
        ):
            newposrow = pos[0]
            if dir[0] > 0:
                while newposrow > 0 and map[newposrow][1] <= newposcol < map[newposrow][
                    1
                ] + len(map[newposrow][0]):
                    newposrow -= 1
                if newposcol < map[newposrow][1] or newposcol >= map[newposrow][
                    1
                ] + len(map[newposrow][0]):
                    newposrow += 1
            elif dir[0] < 0:
                while newposrow < len(map) - 1 and map[newposrow][1] <= newposcol < map[
                    newposrow
                ][1] + len(map[newposrow][0]):
                    newposrow += 1
                if newposcol < map[newposrow][1] or newposcol >= map[newposrow][
                    1
                ] + len(map[newposrow][0]):
                    newposrow -= 1
            else:
                raise Exception("WTF?")
        return newposrow, newposcol
    else:
        newposrow = pos[0]
        newposcol = (
            (pos[1] - map[newposrow][1] + dir[1]) % len(map[newposrow][0])
        ) + map[newposrow][1]
        return newposrow, newposcol

def nextstep2(pos, dir, map):
    # Anpassad för min input
    n = 50
    r, c = pos
    dr, dc = dir
    nr, nc = r+dr, c+dc
    
    if dr == 1:
        if not nr % n:
            match (r // n, c//n):
                case (3,0):
                    nr, nc = 0, 2*n + c 
                case (2,1):
                    nr, nc = 2*n + c, n - 1
                case (0,2):
                    nr, nc = c - n, 2*n - 1
    if dr == -1:
        if not r % n:
            match (r // n, c//n):
                case (2,0):
                    nr, nc = n + c, n
                case (0,1):
                    nr, nc = 2*n + c, 0
                case (0,2):
                    nr, nc = 4*n - 1, c - 2*n
    if dc == 1:
        if not nc % n:
            match (r // n, c//n):
                case (0,2):
                    nr, nc = 3*n - r - 1, 2*n - 1 
                case (1,1):
                    nr, nc = n - 1, n + r
                case (2,1):
                    nr, nc = 3*n - r - 1, 3*n - 1 
                case (3,0):
                    nr, nc = 3*n - 1, r - 2*n
    if dc == -1:
        if not c % n:
            match (r // n, c//n):
                case (0,1):
                    nr, nc = 3*n - r -1, 0 
                case (1,1):
                    nr, nc = 2*n, r - n
                case (2,0):
                    nr, nc = 2*n - c, n
                case (3,0):
                    nr, nc = 0, r - 2*n
    return nr, nc



start_pos = (0, map[0][1])  # start westernmost in northernmost row
start_dir = (0, 1)  # Start east

def partone():
    pos, dir = start_pos, start_dir
    for a in Path(path.strip()):
        if a in {"R", "L"}:
            dir = turn(dir, a)
        else:  # a should be an integer
            for k in range(a):
                newpos = nextstep(pos, dir, map)
                c = get(map, newpos)
                if c == ".":
                    pos = newpos
                elif c == "#":
                    break
                else:
                    raise Exception("Map fault")

    print(
        1000 * (pos[0] + 1)
        + 4 * (pos[1] + 1)
        + {(0, 1): 0, (1, 0): 1, (0, -1): 2, (-1, 0): 3}[dir]
    )

def parttwo():
    pos, dir = start_pos, start_dir
    for a in Path(path.strip()):
        if a in {"R", "L"}:
            dir = turn(dir, a)
        else:  # a should be an integer
            for k in range(a):
                newpos = nextstep2(pos, dir, map)
                c = get(map, newpos)
                if c == ".":
                    pos = newpos
                elif c == "#":
                    break
                else:
                    raise Exception("Map fault")


    print(
        1000 * (pos[0] + 1)
        + 4 * (pos[1] + 1)
        + {(0, 1): 0, (1, 0): 1, (0, -1): 2, (-1, 0): 3}[dir]
)

partone()
parttwo()
for r in range(4):
    for c in [[1,2], [1], [0,1], [0]][r]:
        print(nextstep2((50*r+49, 50*c),(1,0), map))
print("===")
for r in range(4):
    for c in [[1,2], [1], [0,1], [0]][r]:
        print(nextstep2((50*r, 50*c),(-1,0), map))
print("===")
for r in range(4):
    for c in [[1,2], [1], [0,1], [0]][r]:
        print(nextstep2((50*r, 50*c+49),(0,1), map))
print("===")
for r in range(4):
    for c in [[1,2], [1], [0,1], [0]][r]:
        print(nextstep2((50*r, 50*c),(0,-1), map))

