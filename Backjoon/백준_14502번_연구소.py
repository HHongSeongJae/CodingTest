import sys
from collections import deque

input = sys.stdin.readline

n , m = map(int, input().split())

temp = [[0] * m for _ in range(n)] # 벽 설치 후의 맵

# 초기 입력 받는 맵
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

#좌우 상하
dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = 0
# bfs를 이용해 바이러스가 퍼지는 상황 구현
# def virus(x,y):
#     queue = deque()
#     queue.append((x,y))

#     while queue:
#         a,b = queue.popleft()

#         # 4방향 확인
#         for i in range(4):
#             nx = a + dx[i]
#             ny = b + dy[i]

#             if nx < 0 or nx >=n or ny < 0 or ny >= m: # 범위 벗어나는 경우 
#                 continue
                
#             # 벽 무시
#             if temp[nx][ny] == 1:
#                 continue

#             # 빈칸(0)은 2로 바꾼다
#             if temp[nx][ny] == 0:
#                 temp[nx][ny] = 2
#                 queue.append((nx,ny))

#DFS
def virus(x,y):
    # 4방향 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        #범위 내부
        if nx >= 0 and nx <n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx,ny)

#벽 세우기 
def wall(count):
    global result

    # 벽을 3개 세웠다면 바이러스를 퍼뜨린다.
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]

        # 2가 있는 곳이 bfs의 출발지점으로 하면 바이러스가 퍼지는 것 구현 가능
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)

        #안전영역 개수 카운트
        safe = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    safe += 1
        result = max(result, safe)
        return

    # 벽 세우기 ★★ 백트래킹!!
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1 # 벽 세운다
                count += 1
                wall(count) # 다음 벽을 세운다.
                graph[i][j] = 0 # wall에서 return후 들어간다.
                count -= 1 # 벽을 허무는 과정

wall(0)
print(result)
