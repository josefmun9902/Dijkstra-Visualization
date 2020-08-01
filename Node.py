class Node:

	# VARIABLES
	isStart = None
	isEnd = None
	isVisited = None

	#FUNCTIONS
	def __init__(self, isStart, isEnd, isVisited):
		self.isStart = isStart
		self.isEnd = isEnd
		self.isVisited = isVisited