gridSpecs = input().split(" ")

gridRows = int(gridSpecs[0])
gridCols = int(gridSpecs[1])

grid = []

for i in range(gridRows):
    row = input().split(" ")
    grid.append(row)
    
print(grid)

def getSmallerNeighbors(Col, Row):
    me = grid[Col][Row]
    if Col == gridCols:
        dontCheckRight = False
    if Col == 0:
        dontCheckLeft = False
    if Row == gridRows:
        dontCheckDown = False
    if Row == 0:
        dontCheckUp = False
        
    possibleCoords = [[Col-1, Row-1], [Col, Row-1], [Col+1, Row-1], [Col-1, Row], [Col+1, Row], [Col-1, Row+1], [Col, Row+1], [Col+1, Row+1]]
    
    for coord in possibleCoords:
        if coord[0] < 0 or coord[0] > gridCols or coord[1] < 0 or coord[1] > gridRows:
            possibleCoords.pop(coord)
    

    return NeighborList
    
    
def getLongPath(Col, Row):
    Neighbors = getSmallerNeighbors(Col, Row)
