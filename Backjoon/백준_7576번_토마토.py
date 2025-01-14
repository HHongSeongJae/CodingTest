# 퍼질 수 있는 방향 (상하좌우)
# 익은 토마토(1) , 익지 않은 토마토 (0) , 토마토가 없는 칸 (-1)
# 가로(M) -> y / 세로(N) -> x

import sys
from collections import deque

input = sys.stdin.readline

# 방향
dx = [-1,1,0,0]
dy = [0,0,-1,1]

m,n=map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

# 처음부터 모두 익은 토마토로 구성되어있는지를 확인
ok1 = 0
for check in graph:
    if 0 in check: # 하나라도 익지 않은 토마토가 있다면 검사 필요 없다.
        ok1 = 1
        break

# ok1 == 0 이라면 처음부터 모두 익은 토마토로 구성되어있다.
if ok1 == 0:
    print("0")
    exit()

queue = deque()

# 방문을 시작할 좌표
# 익은 토마토에서부터 BFS 방문을 시작
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1: # 익은 토마토는 방문
            visited[i][j] = 0
            queue.append((i,j))

##BFS 방문 시작
while queue:
    xx, yy = queue.popleft()

    for d in range(4):
        nx = xx + dx[d]
        ny = yy + dy[d]

        if 0 <= nx < n and 0 <= ny < m:
            # 인접한 위치는 익지않은 토마토일 경우에만 방문 + 아직 방문하지 않음
            if graph[nx][ny] == 0 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[xx][yy] + 1 # 가중치 업데이트
                graph[nx][ny] = 1 # 익은 토마토로 변경
                queue.append((nx,ny))

# BFS 방문이 끝났을 때 visited에 저장된 가장 큰 값이 모든 토마토를 익게 만드는 최소 일수가 된다.
res = -int(1e9)
for gg in visited:
    res = max(res , max(gg))

# 모두 익지 못하는 상황 확인
ok = 0
for gi in graph:
    if 0 in gi: # 하나라도 익지 않은 토마토(1)가 존재하면 모두 익지 못하는 상황
        ok = 1
        break

# 모두 익지 못하는 상황
if ok == 1:
    print("-1")
else:
    print(res)