def read_input(filename):
    with open(filename) as f:
        input = f.readlines()
    words = [line.strip().split() for line in input]
    return words


def count_it(line_iter, path):
    global totalsum, dirsizelist
    dirsum = 0  # Startar på ny kula
    # vi kör try för att fånga upp vid StopIteration
    try:
        while True:
            words = next(line_iter)
            if words[0] == "$":
                if words[1] == "cd":
                    if words[2] == "..":
                        pass
                        # backar ur. nu bör vi returnera, men också vid filslut
                        # eftersom det inte backas tillbaks på slutet
                        if dirsum <= limit:
                            totalsum += dirsum
                        dirsizelist.append(dirsum)
                        return dirsum
                    else:
                        # nu går vi ner ett steg
                        # för skojs skull och debuggning håller vi koll på path
                        dirsum += count_it(line_iter, f"{path}/{words[2]}")
                elif words[1] == "ls":
                    pass
                    # från nästa rad listas alla filer och underbibliotek, därefter
                    # görs cd ner på underbiblioteken osv rekursivt
                else:
                    pass
            else:
                if words[0] == "dir":
                    pass
                else:
                    # läser storleken och adderar det till dirsum
                    # för det här biblioteket
                    size = int(words[0])
                    dirsum += size
    except StopIteration:
        if dirsum <= limit:
            totalsum += dirsum
        dirsizelist.append(dirsum)
        return dirsum


limit = 100000
totalsum = 0
dirsizelist = []
total = count_it(iter(read_input("input.txt")), "")
free = 70000000 - total
deletesize = 30000000 - free
print(totalsum)
dirsizelist.sort()
for size in dirsizelist:
    if size >= deletesize:
        print(size)
        break
