with open("input0.txt") as f:
    input0 = f.readlines()
with open("input1.txt") as f:
    input1 = f.readlines()

def get_crates(input):
    crates = []
    for line in input:
        linestripped = line.strip()
        if linestripped:
            crates.append(list(linestripped))
    return crates

def get_moves(input):
    moves = []
    for line in input:
        linestripped = line.strip()
        try:
            splits = linestripped.split()
            moves.append([int(splits[k]) for k in [1,3,5]])
        except:
            print("Line omitted:", linestripped)
    return moves

def partone():
    crates = get_crates(input0)
    moves = get_moves(input1)
    for move in moves:
        for k in range(move[0]):
            crates[move[2]-1].append(crates[move[1]-1].pop())
    return ''.join(crate[-1] for crate in crates)

def parttwo():
    crates = get_crates(input0)
    moves = get_moves(input1)
    for move in moves:
        crates[move[2]-1] += crates[move[1]-1][-move[0]:]
        for k in range(move[0]):
            crates[move[1]-1].pop()
    return ''.join(crate[-1] for crate in crates)

print(partone())
print(parttwo())
