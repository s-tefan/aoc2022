def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]

def partone(filename):
    x = 1
    storex = False
    cycle = 1
    countdown = 0
    program = iter(read_input(filename))
    value = 0
    result = 0
    try:
        while program:
            cycle += 1
            if countdown:
                pass
                countdown -= 1
                x += value
                value = 0
            else:
                op = next(program).split()
                if op[0] == 'addx':
                    value = int(op[1])
                    countdown = 1
                elif op[0] == 'noop':
                    countdown = 0
            if cycle in {20,60,100,140,180,220}:
                print(cycle,x, cycle*x)
                result += cycle*x
    except StopIteration:
        print('Klar')
    return result

print(partone("input.txt"))