from collections import deque
n = int(input())
moves = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (-2,1), (2,-1), (-2,-1)]
board = [[None] * n for _ in range(n)]

def bfs(x,y):
    board[x][y] = 'W'
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for dx,dy in moves:
            if 0 <= x+dx < n and 0 <= y+dy < n and not board[x+dx][y+dy]:
                if board[x][y] == 'W':
                    board[x+dx][y+dy] = 'B'
                else:
                    board[x+dx][y+dy] = 'W'
                q.append((x+dx,y+dy))

for x in range(n):
    for y in range(n):
        if not board[x][y]:
            bfs(x,y)

for x in range(n):
    print(''.join(board[x]))

