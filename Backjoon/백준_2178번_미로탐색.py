'''
1은 이동할 수 있는 칸
0은 이동할 수 없는 칸

(1,1) -> (N,M) :: 서로 인접한 칸만 이동이 가능하다.
'''
# from collections import deque

# n ,m = map(int,input().split())

# graph = []
# for _ in range(n):
#     graph.append(list(map(int,input())))


# # 방향 벡터
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def bfs(x,y):
#     queue = deque()
#     queue.append((x,y))

#     while queue:
#         x,y = queue.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             #미로 범위 벗어남
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
            
#             #갈 수 없는 경로 무시
#             if graph[nx][ny] == 0:
#                 continue
#             #갈 수 있는 경로
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx,ny))
#     return graph[n-1][m-1]

# print(bfs(0,0))


### 24.07.10 재풀이

'''
미로같은 맵 문제 -> bfs로 탐색하며 1(갈 수 있는 경로)이면 통과
'''

import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().strip())))  ## sys.readline은 기본적으로 \n\n을 가지고 있기 때문에 strip() 메소드를 통해서 제거

# print(graph)

## 4방향
## 4방향 확인하며 1이면 이동
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

            ## 맵 범위 내부
            if (0 <= nx < n) and (0 <= ny < m):
                ## 갈 수 없는 경로 무시
                if graph[nx][ny] == 0:
                    continue
                
                ## 갈 수 있는 경로이면 이전 경로의 값에 +1 한 후 현재 경로의 값을 업데이트 후 큐에 넣는다.
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))
    return graph[n-1][m-1] # 결과적으로 (n,m) 지점이 지나온 경로의 값이 된다.

print(bfs(0,0))

