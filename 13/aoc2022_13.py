def compare(a, b):
    print(a, b)
    if isinstance(a, int) and isinstance(b, int):
        if a == b:
            return None
        else:
            return a < b
    if isinstance(a, int):
        return compare([a], b)
    if isinstance(b, int):
        return compare(a, [b])
    if a == []:
        return None if b == [] else True
    if b == []:
        return False
    c = compare(a[0], b[0])
    return compare(a[1:], b[1:]) if c == None else c


with open("input.txt") as f:
    pair, k, indices, packets = [], 0, [], []
    while line := f.readline():
        if linestrip := line.strip():
            packets.append(eval(linestrip))
            pair.append(eval(linestrip))
            if len(pair) == 2:
                k += 1
                c = compare(*pair)
                if c:
                    indices.append(k)
                pair = []

import functools

k, dividers = 0, []
packets.append([[2]])
packets.append([[6]])
packets.sort(key=functools.cmp_to_key(lambda x, y: -1 if compare(x, y) else 1))
for p in packets:
    k += 1
    if p == [[2]] or p == [[6]]:
        dividers.append(k)
print(sum(indices))
print(dividers[0] * dividers[1])
