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


def print_diagram(topp, bott):
    for r in range(topp, bott - 1, -1):
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

filename = "test.txt"
with open(filename) as f:
    jets = f.read().rstrip()

n = 0  # position in jets, changes in getjet()
top = 0
fallen = set()


# Part one
for k in range(2022):
    falling_block = Block(order[k % 5], top)
    while True:
        # print_diagram(top + 7, 0)
        falling_block.push(getjet(jets))
        if not falling_block.fall():
            fallen.update(falling_block.block)
            top = max(b[0] for b in fallen)
            break

print(top)

# Part two

n = 0  # position in jets, changes in getjet()
top = 0
fallen = set()
k = 0
startblock_nr = 0
condition_list = []
top_list = []
while True:
    condition = (n, k % 5, fallen)
    if condition in condition_list:
        print(condition_list.index(condition))
        #print(k, condition)
        break
    else:
        condition_list.append(condition)
    falling_block = Block(order[(k+startblock_nr) % 5], top)
    k += 1
    while True:
        falling_block.push(getjet(jets))
        if not falling_block.fall():
            fallen.update(falling_block.block)
            top = max(b[0] for b in fallen)
            top_list.append(top)
            break

# kk = rounds when recurring condition is observed (first round = 0)
kf = condition_list.index(condition) # round for recurring condition
period = k - kf 
period_topping = top-top_list[kf]
#nn = 1_000_000_000_000
nn = 2022
nnn = nn - kf 
periods = nnn // period
left = nnn % period

#top = 0
nö, startblock_nr, fallenö = condition

for k in range(left):
    falling_block = Block(order[(k+startblock_nr) % 5], top)
    k += 1
    while True:
        falling_block.push(getjet(jets))
        if not falling_block.fall():
            fallen.update(falling_block.block)
            top = max(b[0] for b in fallen)
            break

print(top + period_topping*periods)



'''
platt_efter = []
for kk, type in enumerate(order):
    n = 0  # position in jets, changes in getjet()
    top = 0
    fallen = set()
    platt = False
    k = 0
    while not platt:
        falling_block = Block(order[(k+kk) % 5], top)
        k += 1
        while True:
            falling_block.push(getjet(jets))
            if not falling_block.fall():
                fallen.update(falling_block.block)
                top = max(b[0] for b in fallen)
                if {(top,c) for c in range(7)}.issubset(fallen):
                    print(f'platt efter {k} på {top}')
                    platt = True
                    platt_efter.append((k,top))
                break

after = []
for m in range(5):
    a, b = platt_efter[m]
    after.append((m + a) % 5)
print(after)

period = [0]
going = True
while going:
    next_start = after[period[-1]]
    if next_start not in period:
        going = False
    period.append(next_start)

print(period)

## ad hoc härefter
nn = 1_000_000_000_000
start = platt_efter[1][0]
nnn = nn - start
per = platt_efter[1][0]
kvar = nnn % per
antal = nnn // per

# reset everything, kk is the starting block type nr
n = 0  # position in jets, changes in getjet()
top = 0
fallen = set()
kk = 0
for k in range(start + antal*per, nn):
    falling_block = Block(order[(k+kk)%5], top)
    falling_block = Block(order[k%5], top)
    while True:
        # print_diagram()
        falling_block.push(getjet(jets))
        if not falling_block.fall():
            fallen.update(falling_block.block)
            top = max(b[0] for b in fallen)
            break
print(top)    
#print_diagram(top + 7, top -7)

print(platt_efter[0][1] + antal*(platt_efter[1][1]) + top)
'''
