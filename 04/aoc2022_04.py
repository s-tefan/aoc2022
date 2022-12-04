with open("input.txt") as f:
    input = f.readlines()


def getdata(line):
    pair = line.strip().split(",")
    return [int(p) for s in pair for p in s.split("-")]


def check(line):
    data = getdata(line)
    return (data[0] <= data[2] and data[1] >= data[3]) or (
        data[0] >= data[2] and data[1] <= data[3]
    )


def check2(line):
    data = getdata(line)
    return data[1] >= data[2] and data[0] <= data[3]


def partone(input):
    return [check(line) for line in input].count(True)


def parttwo(input):
    return [check2(line) for line in input].count(True)


print(partone(input), parttwo(input))
