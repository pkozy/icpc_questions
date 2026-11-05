N = int(input())

matrix = [[0 for _ in range(N)] for _ in range(N)]

for i in range(1, N+1):
	row = input()
	for j in range(N):
		matrix[i-1][j] = int(row[j])
		
def getColumn(matrix, num):
	col = [0 for _ in range(N)]
	for i in range(N):
		col[i] = int(matrix[i][num])
	return col
	
def getOnez(line):
	count = 0
	for i in range(N):
		if line[i] == 1: count += 1
	return count
	
def getLine(matrix):
	biggestRow = 0
	biggestCol = 0
	for i in range(N):
		current = matrix[i]
		if getOnez(current) > biggestRow: biggestRow = getOnez(current)
	for i in range(N):
		current = getColumn(matrix, i)
		if getOnez(current) > biggestCol: biggestCol = getOnez(current)
	if biggestCol > biggestRow: return "|"
	if biggestRow > biggestCol: return "-"
	if biggestCol == biggestRow: return "+"
	
print(getLine(matrix))
