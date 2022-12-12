def val(node):
    r, c = node
    return ord(elevmap[r][c])

def distance(node, dist_dict):
    if node in dist_dict:
        return dist_dict[node]
    else:
        return float('inf')

def possible(new, old):
    a, b = new
    if a < 0 or a >= nrows:
        return False
    if b < 0 or b >= ncols:
        return False
    if val(old) == ord('S'):
        return True
    if val(new) == ord('E') and val(old) == ord('z'):
        return True
    if not val(new) in range(ord('a'), ord('z')+1):
        return False
    if val(new) <= val(old) + 1:
        return True
    else:
        return False

def possible_back(new, old):
    a, b = new
    if a < 0 or a >= nrows:
        return False
    if b < 0 or b >= ncols:
        return False
    if val(old) == ord('E'):
        return True
    if val(new) == ord('S') and val(old) == ord('a'):
        return True
    if not val(new) in range(ord('a'), ord('z')+1):
        return False
    if val(new) >= val(old) - 1:
        return True
    else:
        return False


def visit(node, dist_dict, visited, backwards = False):
    a, b = node
    d = distance(node, dist_dict) + 1
    for n in {(a-1,b),(a+1,b),(a,b-1),(a,b+1)}:
        # behöver kolla så n inte är utanför eller besökt
        if (possible_back(n, node) if backwards else possible(n, node)) and n not in visited:
            if distance(n, dist_dict) >= d:
                dist_dict[n] = d
    visited.add(node)

with open("input.txt") as f:
    rows = [line.strip() for line in f.readlines()]
    nrows, ncols = len(rows), len(rows[0])
    elevmap = rows

def dijkstra(start, backwards = False):
    current = start
    dist_dict = {current: 0}
    visited = set()
    visit(current, dist_dict, visited, backwards)

    if not backwards:
        while val(current) != ord('E'):
            known_unvisited_set = set(dist_dict).difference(visited)
            if not known_unvisited_set:
                return None
            known_unvisited_dict = {k: dist_dict[k] for k in known_unvisited_set}
            current = min(known_unvisited_dict, key = lambda x: dist_dict[x])
            visit(current, dist_dict, visited)
        return dist_dict[current], current
    else:
        while val(current) != ord('a'):
            known_unvisited_set = set(dist_dict).difference(visited)
            if not known_unvisited_set:
                return None
            known_unvisited_dict = {k: dist_dict[k] for k in known_unvisited_set}
            current = min(known_unvisited_dict, key = lambda x: dist_dict[x])
            visit(current, dist_dict, visited, backwards)
        return dist_dict[current], current
        

dist, goal = dijkstra((0,0)) 
print(dist)
dist, goal = dijkstra(goal, backwards = True)
print(dist)


        