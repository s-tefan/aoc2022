filename = 'input.txt'
with open(filename) as f:
    data = tuple(int(x) for x in f.read().split())


print(data)
print(len(data), len(set(data)))
mupp = list(data)

pos = 0
for k in data:
    pos += k
    mupp.insert(pos, k)

