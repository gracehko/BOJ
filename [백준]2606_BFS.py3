from collections import deque

v = int(input()) # 컴퓨터의 수
e = int(input()) # 연결되어 있는 컴퓨터의 수

graph = [[] for _ in range(v+1)]
visited = [0] * (v+1)

for _ in range(e):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

count=0
visited[1]=1
queue=deque([1])
while queue:
    node=queue.popleft()
    for i in graph[node]:
        if not visited[i]:
            queue.append(i)
            visited[i]=1
            count+=1

print(count)