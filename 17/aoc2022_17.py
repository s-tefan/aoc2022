class Block:
    FLAT = {(4, 2), (4, 3), (4, 4), (4, 5)}
    CROSS = {(4, 3), (5, 2), (5, 3), (5, 4), (6, 3)}
    ANGLE = {
        (4, 2),
        (4, 3),
        (4, 4),
        (5, 4),
        (6, 4),
    }
    STAND = {(4, 2), (5, 2), (6, 2), (7, 2)}
    BLOCK = {(4, 2), (4, 3), (5, 2), (5, 3)}

    def __init__(self, type, top):
        self.block = {(top + t[0], t[1]) for t in type}

    def fall(self):
        newblock = {(r - 1, c) for (r, c) in self.block}
        if max([x[0] for x in newblock]) <= 0:
            return False  # Hit bottom
        if newblock.intersection(fallen):
            return False  # Hit rock
        else:
            self.block = newblock
            return True

    def push(self, dir):
        if dir == "<":
            newblock = {(r, c - 1) for (r, c) in self.block}
        elif dir == ">":
            newblock = {(r, c + 1) for (r, c) in self.block}
        else:
            raise Exception("Fel input")
        if min(x[1] for x in newblock) >= 0 and max(x[1] for x in newblock) <= 6:
            if not newblock.intersection(fallen):
                self.block = newblock


def print_diagram():
    for r in range(top + 7, 0, -1):
        row = ""
        for c in range(7):
            blopp = "#" if (r, c) in fallen else "."
            if (r, c) in falling_block.block:
                blopp = "@"
            row += blopp
        print(row)
    print("-------")


def getjet(jets):
    global n
    c = jets[n]
    n += 1
    if n >= len(jets):
        n = 0
    return c


order = [Block.FLAT, Block.CROSS, Block.ANGLE, Block.STAND, Block.BLOCK]

filename = "input.txt"
with open(filename) as f:
    jets = f.read().rstrip()
n = 0  # position in jets, changes in getjet()
top = 0
fallen = set()

for k in range(2022):
    falling_block = Block(order[k % 5], top)
    while True:
        # print_diagram()
        falling_block.push(getjet(jets))
        if not falling_block.fall():
            fallen.update(falling_block.block)
            top = max(b[0] for b in fallen)
            break
print(top)
