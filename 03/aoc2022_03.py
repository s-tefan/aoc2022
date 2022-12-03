with open("input.txt") as f:
    input = f.readlines()


def priority(c):
    asc = ord(c)
    if asc >= ord("a"):
        return asc - ord("a") + 1
    else:
        return asc - ord("A") + 27


def mupp(linestrip):
    divider = len(linestrip) // 2
    a, b = linestrip[:divider], linestrip[divider:]
    common = set(a).intersection(b)
    return sum(priority(c) for c in common)


def mopp(grouplines):
    badgeset = set.intersection(*[set(line.strip()) for line in grouplines])
    if len(badgeset) != 1:
        raise Exception("Not a single common item among group members")
    return priority(badgeset.pop())


def partone(input):
    return sum(mupp(line.strip()) for line in input)


def parttwo(input):
    return sum(mopp(input[3 * k : 3 * (k + 1)]) for k in range(len(input) // 3))


print(partone(input))
print(parttwo(input))
