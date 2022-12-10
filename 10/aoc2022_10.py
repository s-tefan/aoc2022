def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]

def partone(filename):
    cycle, x, countdown, value  = 0, 1, 0, 0
    program = iter(read_input(filename))
    result = 0
    crt = ''
    try:
        while True:
            cycle += 1
            pos = (cycle-1)%40
            pix = 'x' if pos in range(x-1,x+2) else '.'
            if cycle in {20,60,100,140,180,220}:
                result += cycle*x
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
            # Add pixel at the end to catch StopIteration before
            crt += pix + ('' if cycle%40 else '\n')
            
    except StopIteration:
        print('Klar')
    return result, crt

for result in partone("input.txt"):
    print(result)