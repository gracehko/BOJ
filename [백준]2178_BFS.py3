from collections import deque

n, m = map(int, input().split())
maze = []

for i in range(n):
    maze.append(list(map(int, input())))

dx = [0, 0, 1, -1] #좌,우
dy = [1, -1, 0, 0] #상,하

def bfs(i,j):
    queue=deque()
    queue.append((i,j))

    while queue:
        x, y= queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if maze[nx][ny]==1:
                    maze[nx][ny]=maze[x][y]+1
                    queue.append((nx,ny))
    return maze[n-1][m-1]

print(bfs(0,0))
