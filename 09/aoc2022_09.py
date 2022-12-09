def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]

translation = {'R':(1,0), 'L':(-1,0), 'U':(0,1), 'D': (0,-1)}

def vector_add(p, v):
    for k, c in enumerate(v):
        p[k] += c

def read_move(line):
    a = line.split()
    return {'dir': translation[a[0]], 'steps': int(a[1])}

def update_tail(tail, head):
    diff = [head[k]-tail[k] for k in range(2)]
    # if touching: return
    if all(abs(k) < 2 for k in diff):
        return
    # if one of the components == 0 move in the other
    for k in [0,1]:
        if diff[1-k] == 0:
            tail[k] += (1 if diff[k]>0 else -1 if diff[k]<0 else 0)
            return
    # otherwise move diagonally
    for k in [0,1]:
        tail[k] += (1 if diff[k]>0 else -1 if diff[k]<0 else 0)
    return


def diagram(s, n):
    for k in range(n):
        for m in range(n):
            if (m,n-k-1) in s:
                print('#',end='')
            else:
                print('.',end='')
        print()


def partone(input):
    hpos = [0,0]
    tpos = [0,0]
    tail_visited = {tuple(tpos)}
    for move in [read_move(line) for line in input]:
        for step in range(move['steps']):
            vector_add(hpos, move['dir'])
            update_tail(tpos, hpos)
            tail_visited.add(tuple(tpos))
    return tail_visited

def parttwo(input):
    hpos = [0,0]
    n = 10
    knots = [[0,0] for k in range(n)]
    tail_visited = {tuple(knots[-1])}
    for move in [read_move(line) for line in input]:
        for step in range(move['steps']):
            vector_add(knots[0], move['dir'])
            for k in range(n-1):
                update_tail(knots[k+1], knots[k])
            tail_visited.add(tuple(knots[-1]))
    return tail_visited


print(len(partone(read_input("input.txt"))))
print(len(parttwo(read_input("input.txt"))))

