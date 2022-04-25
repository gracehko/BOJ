from collections import deque

m, n = map(int, input().split())
tomato=[]
queue=deque([])
for i in range(n):
    tomato.append(list(map(int, input().split())))
    for j in range(m):
        if tomato[i][j]==1:
            queue.append([i,j])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and tomato[nx][ny]==0:
                tomato[nx][ny]=tomato[x][y]+1
                queue.append([nx,ny])

bfs()
days=0
for i in tomato:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    days=max(days, max(i))

print(days-1)