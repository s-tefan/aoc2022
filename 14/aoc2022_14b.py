def genrange(a, b):
    if a > b:
        return range(b, a + 1)
    elif a == b:
        return range(a, a + 1)
    else:
        return range(a, b + 1)


rock = set()
with open("input.txt") as f:
    for words in [line.strip().split(" -> ") for line in f.readlines()]:
        last = None
        for word in words:
            node = eval(word)
            if last:
                for x in genrange(last[0], node[0]):
                    for y in genrange(last[1], node[1]):
                        rock.add((x, y))
            last = node
            rock.add((node[0], node[1]))

ymax = max(stone[1] for stone in rock)


start, k = (500, 0), 1
while True:
    pos = start
    while y <= ymax + 1:
        x, y = pos
        if not (x, y + 1) in rock and y <= ymax:
            pos = (x, y + 1)
        elif not (x - 1, y + 1) in rock and y <= ymax:
            pos = (x - 1, y + 1)
        elif not (x + 1, y + 1) in rock and y <= ymax:
            pos = (x + 1, y + 1)
        else:
            rock.add(pos)
            break
    if pos == start:
        break
    k += 1


print(k)
