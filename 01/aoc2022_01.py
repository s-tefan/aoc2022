with open("input.txt") as f:
    input = f.readlines()

cal = 0
calories = []
for line in input:
    if k := line.strip():
        cal += int(k)
    else:
        calories.append(cal)
        cal = 0
if cal:
    calories.append(cal)
maxcals = max(calories)
#maxcalsindex = calories.index(maxcals)
print(maxcals)
calories.sort(reverse = True)
print(sum(calories[:3]))
