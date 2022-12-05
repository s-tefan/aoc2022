import readinput

def partone():
    crates, moves = readinput.read_input("input.txt")
    for move in moves:
        for k in range(move[0]):
            crates[move[2]-1].append(crates[move[1]-1].pop())
    return ''.join(crate[-1] for crate in crates)

def parttwo():
    crates, moves = readinput.read_input("input.txt")
    for move in moves:
        crates[move[2]-1] += crates[move[1]-1][-move[0]:]
        del crates[move[1]-1][-move[0]:]
    return ''.join(crate[-1] for crate in crates)

print(partone())
print(parttwo())
