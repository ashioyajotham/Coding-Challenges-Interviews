board = [['r', 'a', 'e', 'l'],
			['m', 'o', 'f', 's'],
			['t', 'e', 'o', 'k'],
			['n', 'a', 't', 'i']]

words = dict() # assumes words are added
result = []

findWords(board)

def findWords(board):
	visited = set()
	word = ""

	for i in range(len(board)):
		for j in range(len(board)):
			dfs(word, i, j, visited)

def reachable(i, j, visited):
	return (i, j) not in visited and (i < len(board) and i >= 0) and (j < len(board) and j >= 0)

def dfs(word, i, j, visited):
	word = word + board[i][j]

	if word in board:
		result += [word]
		visited.pop((i, j))
		return

	visited.add((i, j)) # temporarily mark where we've been so we don't keep visiting the same place

	# go all possible directions to simulate all paths
	if reachable(i + 1, j, visited):
		dfs(word, i + 1, j, visited)

	if reachable(i - 1, j + 1, visited):
		dfs(word, i - 1, j + 1, visited)

	if reachable(i, j + 1, visited):
		dfs(word, i, j + 1, visited)

	if reachable(i + 1, j + 1, visited):
		dfs(word, i + 1, j + 1, visited)

	if reachable(i - 1, j - 1, visited):
        dfs(word, i - 1, j - 1, visited)

	if reachable(i, j - 1, visited):
		dfs(word, i, j - 1, visited)

	if reachable(i + 1, j - 1, visited):
		dfs(word, i + 1, j - 1, visited)

	if reachable(i - 1, j, visited):
		dfs(word, i - 1, j, visited)	


	visited.pop((i, j))
