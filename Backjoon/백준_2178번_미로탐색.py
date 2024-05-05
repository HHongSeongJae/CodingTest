'''
1은 이동할 수 있는 칸
0은 이동할 수 없는 칸

(1,1) -> (N,M) :: 서로 인접한 칸만 이동이 가능하다.
'''
from collections import deque

n ,m = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input())))


# 방향 벡터
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #미로 범위 벗어남
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            #갈 수 없는 경로 무시
            if graph[nx][ny] == 0:
                continue
            #갈 수 있는 경로
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))

