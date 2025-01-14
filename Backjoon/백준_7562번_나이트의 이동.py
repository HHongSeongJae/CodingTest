import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

# 방향
dx = [-2,-2,-1,1,2,2,1,-1]
dy = [-1,1,2,2,1,-1,-2,-2]

res = []

for _ in range(t):
    l = int(input())

    graph = [[-1] * l for _ in range(l)]

    startx , starty = map(int,input().split())
    x , y = map(int,input().split())

    if startx == x and starty == y:
        res.append(0)
        continue

    queue = deque()
    queue.append((startx, starty))
    graph[startx][starty] = 0

    while queue:
        xx, yy = queue.popleft()

        if xx == x and yy == y:
            break

        for i in range(8):
            nx = xx + dx[i]
            ny = yy + dy[i]

            if 0 <= nx < l and 0 <= ny < l:
                if graph[nx][ny] == -1:
                    graph[nx][ny] = graph[xx][yy] + 1
                    queue.append((nx,ny))

    res.append(graph[x][y])

for r in res:
    print(r)