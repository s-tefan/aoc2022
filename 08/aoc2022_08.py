def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]


def check(row):
    vislist, largest = [], -1
    for k, tree in enumerate(row):
        if int(tree) > largest:
            vislist.append(k)
            largest = int(tree)
            if largest >= 9:
                break
    return vislist


def partone(lines):
    grove = lines
    visible = set()
    for rownr, row in enumerate(grove):
        for nr in check(row):
            visible.add((rownr, nr))
        for nr in check(reversed(row)):
            visible.add((rownr, len(row) - nr - 1))
    grovetransposed = [[row[k] for row in grove] for k in range(len(grove[0]))]
    for rownr, row in enumerate(grovetransposed):
        for nr in check(row):
            visible.add((nr, rownr))
        for nr in check(reversed(row)):
            visible.add((len(row) - nr - 1, rownr))
    return len(visible)


def parttwo(lines):
    grove = lines
    nrows = len(grove)
    maxscenic = 0

    def view(treelist, height):
        k = -1  # in case treelist is empty
        for k, othertree in enumerate(treelist):
            if int(othertree) >= height:
                break
        return k + 1

    for rownr, row in enumerate(grove):
        for colnr, tree in enumerate(row):
            height = int(tree)
            east = view(row[colnr + 1 :], height)
            west = view(reversed(row[:colnr]), height)
            south = view([grove[i][colnr] for i in range(rownr + 1, nrows)], height)
            north = view([grove[i][colnr] for i in reversed(range(rownr))], height)
            scenic = east * west * north * south
            if scenic > maxscenic:
                maxscenic = scenic
    return maxscenic


lines = read_input("input.txt")
print(partone(lines))
print(parttwo(lines))
