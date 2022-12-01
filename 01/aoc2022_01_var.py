with open("input.txt") as f:
    input = f.readlines()

class Pall():
    def __init__(self, n):
        self.pallist = []
        self.n = n
    def nominate(self, value):
        if not self.pallist:
            self.pallist.append(value)
            return
        elif value <= self.pallist[-1]:
            return
        else:
            if len(self.pallist) >= self.n:
                self.pallist.pop(-1)
            self.pallist.append(value)
            self.pallist.sort(reverse = True)
            return
    def topp(self):
        return self.pallist[0]
    def summa(self):
        return sum(self.pallist)
    

cal = 0
topptre = Pall(3)
for line in input:
    if k := line.strip():
        cal += int(k)
    else:
        topptre.nominate(cal)
        cal = 0
if cal:
    topptre.nominate(cal)
print(topptre.topp())
print(topptre.summa())
