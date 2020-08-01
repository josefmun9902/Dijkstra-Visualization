class Node:

    # VARIABLES
    isStart = None
    isEnd = None
    isVisited = None
    distanceToNode = 999
    gridRow = None
    gridColumn = None

    #FUNCTIONS
    def __init__(self, isStart, isEnd, isVisited, gridRow, gridColumn):
        self.isStart = isStart
        self.isEnd = isEnd
        self.isVisited = isVisited
        self.gridRow = gridRow
        self.gridColumn = gridColumn