# 안전영역 -> BFS

'''
- 입력 받은 그래프의 노드를 순회하면서 N이하의 숫자가 위치하는 곳은 0으로 바꾼다.

- BFS : 0을 만나면 탈출

* 비가 언제까지 올지 모르는 상황에서 물에 잠기지 않는 안전한 영역의 최대 개수!!
'''

# from collections import deque

# N = int(input())
# city = []

# for i in range(N):
#     city.append(list(map(int,input().split())))

# # 비가 올 수 있는 물의 최대량을 구한다.
# # 비가 어느정도 내릴지 모르는 상황이기 때문에 max로 올 수 있는 양을 구한다.
# maxRain = 0
# for i in range(N):
#     for j in range(N):
#         if city[i][j] > maxRain:
#             maxRain = city[i][j]

# # 상하좌우 확인을 위한 방향 벡터
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# # BFS
# def bfs(x , y):
#     global count

#     # 큐 선언
#     queue = deque()
#     queue.append((x,y)) # 현재 방문한 위치

#     # 방문 처리
#     check[x][y] = 1
#     count += 1

#     # 큐가 비는 상황까지 반복
#     while queue:
#         x,y = queue.popleft()

#         # 4방향 확인
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             # 영역 내부의 경우에만 유효
#             if nx < 0 or nx >= N or ny < 0 or ny >= N:
#                 continue

#             # 상하좌우 잠기지 않은 부분 찾기
#             if check[nx][ny] == 0:
#                 check[nx][ny] = 1 # 잠긴 것으로 처리
#                 queue.append((nx,ny))

# count_list = []

# for rain in range(maxRain):
#     count = 0 # 안전영역 개수
#     check = [[ 0 for _ in range(N)] for i in range(N)]

#     for i in range(N):
#         for j in range(N):
#             if city[i][j] <= rain: #잠기는 상황
#                 check[i][j] = 1 # 잠긴 구역

#     # 잠기지 않은 구역에 대해서만 bfs 수행
#     for i in range(N):
#         for j in range(N):
#             if check[i][j] == 0:
#                 bfs(i,j)
#     count_list.append(count)

# print(max(count_list))

import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

city = []
maxRain = 0

# 도시의 높이 확인하기
for _ in range(N):
    city.append(list(map(int,input().split())))

# 최대 높이 찾기
for i in city:
    maxRain = max(max(i) , maxRain)

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# BFS
def bfs(x,y):
    global count

    queue = deque()
    queue.append((x,y))

    visited[x][y] = 1
    count += 1

    while queue:
        xx , yy = queue.popleft()

        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]

            # 유효 범위 확인
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            # 상하좌우 잠기지 않은 부분
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny))

# 비가 오는 경우
countList = []

for r in range(maxRain):
    count = 0 # 안전 영역 개수
    visited = [[0 for _ in range(N)] for _ in range(N)] # 현재 r만큼 비가 왔다는 가정하에 잠긴구역 표시

    # r만큼 비가왔다는 가정하에 잠기는 구역 표시
    for i in range(N):
        for j in range(N):
            if city[i][j] <= r: # 잠긴경우
                visited[i][j] = 1
    
    # bfs
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                bfs(i,j)
    countList.append(count)
    print(countList)

print(max(countList))