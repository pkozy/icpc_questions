def bringAnswer(start, end):
	#print(start)
	#print(end)
	return 2 * (abs(start[0]-end[0]) + abs(start[1]-end[1]))

def getClosest(start, pts):
	shortest = 2000
	closest = pts[0]
	for pt in pts:
		distance = bringAnswer(start, pt)
		if distance < shortest:
			shortest = distance	
			closest = pt
	#print(f"the closest to start {start} is {closest}")
	return closest

def getMinIndex(l):
	mIndex = 0
	lMin = 2000
	for i in range(len(l)):
		item = l[i]
		if item < lMin:
			mIndex = i
			lMin = item
	return mIndex
	
numStudents = int(input())
pts = []

for i in range(numStudents):
	ptInput = input().split(' ')
	pt = [int(ptInput[0]), int(ptInput[1])]
	pts.append(pt)

#print(pts)
distance = 0
smartPts = [pts[0]]
pts.pop(0)

while len(pts) > 0:
	shortestDistances = []
	closestPts = []
	for smtPt in smartPts:
		#print(f"smtPts is {smartPts} and pts is {pts}" )
		closestPt = getClosest(smtPt, pts)
		#print(f"adding {shortestDistance} to distance {distance}")
		#print(f"smartPts is now {smartPts}")
		print(f"closestPt is {closestPt}")
		shortestDistances.append(bringAnswer(closestPt, smtPt))
		closestPts.append(closestPt)
	closestIndex = getMinIndex(shortestDistances)
	closestPt = closestPts[closestIndex]
	
	smartPts.append(closestPt)
	pts.remove(closestPt)
	
	#print(f"the closest pt is {closestPt} for smtPt{smartPts[closestIndex]}")
	
	distance += shortestDistances[closestIndex]
	
		
print(distance)

