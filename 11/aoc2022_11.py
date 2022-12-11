class Monkey:
    def __init__(self, starting_items, operation_string, divisor, throw_to):
        self.items = starting_items
        self.operation_string = operation_string
        self.divisor = divisor
        self.throw_to = throw_to
        self.inspections = 0

    def throw(self, old):
        new = eval(self.operation_string) // 3
        # Return monkey to throw to, item to throw
        return self.throw_to[bool(new % self.divisor)], new

    def throw2(self, old):
        new = eval(self.operation_string) % common_divisor
        # Return monkey to throw to, item to throw
        return self.throw_to[bool(new % self.divisor)], new

    def inspect(self):
        self.inspections += len(self.items)
        throw_list = [self.throw(item) for item in self.items]
        self.items = []
        return throw_list

    def inspect2(self):
        self.inspections += len(self.items)
        throw_list = [self.throw2(item) for item in self.items]
        self.items = []
        return throw_list

    def gets(self, item):
        self.items.append(item)


def read(file):
    monkeylist = []
    while line := file.readline():
        words = line.strip().split()
        if words and words[0] == "Monkey":
            words = file.readline().strip().split()
            expr = "[" + "".join(words[2:]) + "]"
            starting_items = eval(expr)
            words = file.readline().strip().split()
            operation_string = " ".join(words[3:])
            words = file.readline().strip().split()
            divisor = eval(words[3])
            words = file.readline().strip().split()
            if_true = eval(words[5])
            words = file.readline().strip().split()
            if_false = eval(words[5])
            monkeylist.append(
                Monkey(starting_items, operation_string, divisor, (if_true, if_false))
            )
        else:
            pass
    return monkeylist


with open("input.txt") as f:
    monkeylist = read(f)
    for round in range(20):
        for monkey in monkeylist:
            for monkey_number, item in monkey.inspect():
                # print(monkey_number, item)
                monkeylist[monkey_number].gets(item)
    mblist = sorted([monkey.inspections for monkey in monkeylist])
    monkey_business = mblist[-1] * mblist[-2]
    print(monkey_business)

with open("input.txt") as f:
    monkeylist = read(f)
    common_divisor = 1
    for monkey in monkeylist:
        common_divisor *= monkey.divisor
    for round in range(10000):
        for monkey in monkeylist:
            for monkey_number, item in monkey.inspect2():
                # print(monkey_number, item)
                monkeylist[monkey_number].gets(item)
    mblist = [monkey.inspections for monkey in monkeylist]
    #print(mblist)
    mblist.sort()
    monkey_business = mblist[-1] * mblist[-2]
    print(monkey_business)
