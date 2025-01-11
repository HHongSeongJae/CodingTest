from collections import deque

n = int(input())

graph = []

for i in range(n):
    graph.append(list(input().strip())) # 000111와 같이 string형태로 받아지기 때문에 .strip()을 사용해야분리가 된다.

# 각 단지별로 아파트 수를 저장할 리스트
res = []

# 방향 벡터
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,aptcnt):
    queue = deque()
    queue.append((x,y))

    # 집(1)인 칸을 방문하면 이를 방문했음을 구분하기 위해서 0으로 바꾼다.
    graph[x][y] = 0

    while queue:
        xx , yy = queue.popleft()

        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if int(graph[nx][ny]) == 1: # 상하좌우에 1칸이 존재하면 방문
                    graph[nx][ny] = 0
                    aptcnt += 1 # 현재 단지의 아파트수를 센다
                    queue.append((nx,ny))
    return aptcnt # 한 단지의 아파트를 모두 탐색한 상태이므로 단지에 아파트가 몇 개 있는지 return한다.

# nxn 배열을 모두 훑으면서 1인 지점을 시작점으로 bfs를 수행한다.
for ii in range(n):
    for jj in range(n):
        if int(graph[ii][jj]) == 1:
            res.append(bfs(ii,jj,1)) # [ii][jj] 위치에 있는 곳도 아파트 1개이므로 aptcnt의 시작값은 1로 한다.

res.sort() # [문제조건] 각 단지내 집의 수를 오름차순으로 정렬

print(len(res)) # res에 들어있는 숫자의 수는 단지의 수가 된다.
for r in res:
    print(r)