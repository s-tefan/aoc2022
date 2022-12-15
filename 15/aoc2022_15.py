filename, row, rowmax = "input.txt", 2_000_000, 4_000_000
# filename, row, rowmax = 'test.txt', 10, 20


class Point:
    def __init__(self, x=None, y=None):
        self.x, self.y = x, y

    def d(self, p):
        return abs(self.x - p.x) + abs(self.y - p.y)

    def to_tuple(self):
        return (self.x, self.y)


class Sensor:
    def __init__(self, pos=None, beacon=None):
        self.pos, self.beacon = pos, beacon

    def radius(self):
        return self.pos.d(self.beacon)

    def range(self, row):
        halflength = self.radius() - abs(row - self.pos.y)
        if halflength >= 0:
            return range(self.pos.x - halflength, self.pos.x + halflength + 1)
        else:
            return range(0)

    def minmax(self, row):
        halflength = self.radius() - abs(row - self.pos.y)
        if halflength >= 0:
            return self.pos.x - halflength, self.pos.x + halflength
        else:
            return


with open(filename) as f:
    lines = f.readlines()


sensors = []
for line in (l.rstrip().split() for l in lines):
    pos, beacon_pos = Point(), Point()
    pos.x = int(line[2][2:-1])
    pos.y = int(line[3][2:-1])
    beacon_pos.x = int(line[8][2:-1])
    beacon_pos.y = int(line[9][2:])
    sensors.append(Sensor(pos, beacon_pos))


def partone():
    blurp = set()
    beacons_in_row = set()
    for s in sensors:
        blurp.update(s.range(row))
        if s.beacon.y == row:
            beacons_in_row.add(s.beacon.x)
    return len(blurp.difference(beacons_in_row))


def schappa(x, y):
    return x * 4_000_000 + y


def parttwo():
    for row in range(rowmax + 1):
        if not (row % 100000):
            print("*", row)
        rl = []
        for s in sensors:
            if r := s.minmax(row):
                rl.append(r)
        rl.sort()  # 11:o på min
        if rl[0][0] > 0:
            return schappa(0, row)
        joined_interval = rl[0]
        for k, r in enumerate(rl[1:]):
            if r[0] > rowmax:
                break
            if r[0] > joined_interval[1] + 1:
                return schappa(joined_interval[1] + 1, row)
            else:
                if r[1] > joined_interval[1]:
                    joined_interval = (joined_interval[0], r[1])
            if joined_interval[1] >= rowmax:
                break


print(partone())
print(parttwo())
