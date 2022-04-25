from collections import deque
t = int(input())
cnt=[]

dx=[-2,-1,1,2,2,1,-1,-2]
dy=[1,2,2,1,-1,-2,-2,-1]

def bfs(n_x, n_y, f_x, f_y):
    queue=deque()
    queue.append([n_x, n_y])
    chess[n_x][n_y]=1
    while queue:
        x, y=queue.popleft()
        if x==f_x and y==f_y:
            return chess[x][y]-1

        for i in range(8):
            r_x = x + dx[i]
            r_y = y + dy[i]
            if 0<=r_x<l and 0<=r_y<l and chess[r_x][r_y]==0:
                queue.append([r_x,r_y])
                chess[r_x][r_y] = chess[x][y] + 1


for i in range(t):
    l = int(input())
    chess = [[0]*l for _ in range(l)]

    n_x, n_y = map(int, input().split())
    f_x, f_y = map(int, input().split())

    if n_x == f_x and n_y == f_y:
        print(0)
    else:
        print(bfs(n_x, n_y, f_x, f_y))
