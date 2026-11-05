def findClosest(start, beepList):
    min = 50
    closest = None
    for beep in beepList:
        if (distance(start, beep) < min):
            min = distance(start,beep)
            closest = beep
    return closest

def distance(start, end):
    return int(abs(start[0] - end[0]) + abs(start[1] - end[1]))

samples = int(input())

for sample in range(samples):
    size_in = input()
    width = int(size_in.split(" ")[0])
    height = int(size_in.split(" ")[1])
    size = (width, height)

    startpos_in = input()
    x_start = int(startpos_in.split(" ")[0])
    y_start = int(startpos_in.split(" ")[1])
    ogpos = (x_start, y_start)

    numbeep = int(input())
    beepList = []
    for beep in range(numbeep):
        beeppos_in = input()
        beep_x = int(beeppos_in.split(" ")[0])
        beep_y = int(beeppos_in.split(" ")[1])
        beepList.append((beep_x, beep_y))

    final_distance = 0
    startpos = ogpos
    while len(beepList) > 0:
        closest = findClosest(startpos, beepList)
        beepList.remove(closest)
        final_distance += distance(startpos, closest)
        startpos = closest
    final_distance += distance(closest, ogpos)

    print(final_distance)
