filename = "input.txt"
with open(filename) as f:
    data = tuple(eval(line.strip())for line in f)


def count_faces(data, l):
    other = {0,1,2}
    other.discard(l)
    a, b = other
    count = 0
    mn = {tuple(d[j] for j in other) for d in data} 
    for m, n in mn:
            s = sorted([x[l] for x in data if x[a] == m and x[b] == n])
            for k, c in enumerate(s[:-1]):
                if s[k+1] != c + 1:
                    count += 2
            count += 2 # first and last
    return count


count = 0
for i in range(3):
    count += count_faces(data, i)
print(count)