with open("input.txt") as f:
    input = f.readlines()

value = {'A':1, 'B':2,'C':3,'X':1, 'Y':2,'Z':3,}

def match(a,b):
    return 3*((a - b + 1)% 3) 

s1 = 0
s2 = 0
for line in input:
    a, b = line.strip().split(' ')
    x, y = value[a], value[b]
    s1 += match(y,x) + y
    z = (x + y) % 3 + 1
    s2 += 3 * (y - 1) + z 
print(s1)
print(s2)
