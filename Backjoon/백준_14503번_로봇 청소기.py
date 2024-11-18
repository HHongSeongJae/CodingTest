# from collections import deque

# n , m = map(int,input().split())
# r , c , d = map(int,input().split())
# graph = [list(map(int,input().split())) for _ in range(n)]

# res = 1 # 청소한 구역 개수

# # 방향 벡터
# dx = [-1,0,1,0] # (반시계) 북 서 남 동
# dy = [0,-1,0,1]

# # 후진 함수
# def back(x,y,d):
#     global res

#     # d 기준 후진 방향 찾기
#     # back_d = (d + 2) % 4

#     # 후진 방향으로 1칸 이동 (바라보는 방향은 유지)
#     # back_x , back_y = x + dx[back_d] , y + dy[back_d]
#     back_x , back_y = x - dx[d] , y - dy[d]

#     if graph[back_x][back_y] == 1: # 바라보는 방향의 후진 방향이 벽이라 후진 불가
#         return
#     else:
#         #(back_x, back_y) 좌표에서 bfs 함수 호출
#         bfs(graph, back_x , back_y , d)

# # BFS 함수
# def bfs(graph, x, y , d):
#     global res

#     q = deque()
#     q.append((x,y,d))

#     graph[x][y] = 1 # 현재 좌표 방문(청소) 처리

#     while q:
#         xx, yy , dd = q.popleft()

#         # 반시계 방향으로 확인
#         ok = 0
#         for i in range(4):
#             nx = xx + dx[i]
#             ny = yy + dy[i]

#             if graph[nx][ny] == 0:
#                 ok = 1
#                 graph[nx][ny] = 1
#                 res += 1
#                 q.append((nx,ny,i))

#         if ok == 0: # 4방향 청소되지 않은 빈칸이 없을 경우 후진
#             back(xx,yy,dd)

# bfs(graph, r, c , d)

# print(res)

## 오답 :: 해당 문제는 모든 방문을 하는 것이 목적이 아니기 때문에 BFS로 풀이하면 안된다.
n , m = map(int,input().split())
r , c , d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

# 방향 벡터
# 0인 경우 북쪽, 1인 경우 동쪽, 2인 경우 남쪽, 3인 경우 서쪽
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 벽 : 1 , 청소방 : 2 , 청소안한방 : 0
while True:
    # 현재 방문한 좌표를 청소한 좌표로 처리한다.
    if graph[r][c] == 0:
        graph[r][c] = 2

    # 현재 좌표 4방향 확인
    if graph[r-1][c] != 0 and graph[r+1][c] != 0 and graph[r][c-1] != 0 and graph[r][c+1] != 0:
        ## 4방향 모두 청소되지 않는 방이 없다면 현재 방향을 유지한 채로 후진
        backx , backy = r - dx[d] , c - dy[d]
        ## 후진할 좌표가 벽이라면 프로그램 종료
        if graph[backx][backy] == 1:
            break
        else:
            r , c = backx, backy
    ## 반시계 방향으로 회전하며 바라보는 방향의 앞쪽 칸이 청소되지 않는 칸이면 한 칸 전진
    else:
        # 바라보는 방향을 반시계 방향으로 하나씩 이동
        d = (d+3) % 4 # +3씩 이동하면 반시계 방향으로 방향이 이동하는 것을 볼 수 있다.

        # 바라보는 방향 앞쪽 칸이 청소되지 않은 칸이라면 전진
        gox , goy = r + dx[d] , c + dy[d]
        if graph[gox][goy] == 0:
            r , c = gox, goy

# 청소된 방(2) 개수 출력
res = 0
for i in graph:
    res += i.count(2)

print(res)