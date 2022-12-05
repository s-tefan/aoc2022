def read_input(filename):
    with open("input.txt") as f:
    #    input = f.readlines()

        bopper = []
    #for line in input:
        while True:
            line = f.readline()
            bop = line[1::4]
            if bop[0] == '1':
                break
            bopper.append(bop)
        cratestacks = []
        for k, key in enumerate(bop):
            cratestacks.append([])
        bopper.reverse()
        for crates in bopper:
            for k, crate in enumerate(crates):
                if crate != ' ':
                    cratestacks[k].append(crate)
        moves = []
        while True:
            line = f.readline()
            if not line:
                break
            stripline = line.strip()
            if stripline:
                move = line.split()[1::2]
                moves.append([int(n) for n in move])
        return cratestacks, moves