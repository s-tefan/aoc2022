def doit(filename, n):
    with open(filename) as f:
        buffer = f.read(n)
        k = n
        while True:
            if all([x != y for k, x in enumerate(buffer) for y in buffer[k+1:]]):
                break
            buffer = buffer[1:]
            buffer += f.read(1)
            k += 1
        return k    

print(doit('input.txt', 4))
print(doit('input.txt', 14))
