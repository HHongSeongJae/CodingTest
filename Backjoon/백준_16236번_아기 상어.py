from collections import deque

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

# 방향 벡터
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 아기상어 시작 정보
nowx, nowy = -1,-1
now_size = 2

# 아기상어 위치 찾기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            nowx , nowy = i , j
            graph[i][j] = 0 # 상어는 9로 표시되어있다.
                            # 물고기의 크기는 1~6의 크기를 가지고 있다.
                            # 이후에 현재 상어의 크기(now_size)와 방문한 곳의 물고기가 있다면 크기를 비교하여 먹을 수 있는지 / 지날 수 있는지 여부를 판단한다.
                            # 그런데 9라는 숫자가 있다면 이를 따로 조건을 주어야하기 때문에 상어의 현재 위치는 따로 유지하며 graph에서는 0(빈칸)으로 설정정

# BFS를 통해 최단거리를 구하는 함수
def bfs():
    # 최단거리맵 (수행시 마다 최단거리는 최신화되어야 함) (방문하지 않은 곳은 -1)
    dist = [[-1] * n for _ in range(n)]
    
    q = deque()
    q.append((nowx,nowy))
    
    dist[nowx][nowy] = 0 # (nowx,nowy) 좌표가 시작점

    while q:
        xx , yy = q.popleft()

        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] == -1 and graph[nx][ny] <= now_size: # 방문하지 않았던 곳이면서 크기가 현재 상어의 몸집보다 작거나 같으면 통과 가능
                                                                     # 상어의 몸집보다 작은 물고기는 먹을 수 있으며, 같다면 통과할 수 있다.
                    dist[nx][ny] = dist[xx][yy] + 1 # 최단거리 1증가
                    q.append((nx,ny))

    return dist # 최단 거리 표를 리턴한다.

# 먹을 물고기를 찾는 함수
def find(dist):

    # 먹을 수 있는 물고기에 대한 정보
    findx , findy = -1 , -1
    min_dist = int(1e9) # 해당 물고기로 갈 수 있는 최단 경로

    for i in range(n):
        for j in range(n):
            # 도달 가능 + 먹을 수 있는 조건(물고기의 크기가 현재 상어의 크기(now_size)보다 작아야 한다.)
            if dist[i][j] != -1 and 1 <= graph[i][j] < now_size:
                # 최단 거리일 경우에만 갱신
                # i , j 는 1~n 순서로 탐색하기 때문에 먼저나오는 최단거리가 가장 왼쪽 상단에 있는 위치이다.
                # 그래서 '거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다' 에 대한 조건은 여기서 처리가 된다.
                if dist[i][j] < min_dist:
                    findx , findy = i , j
                    min_dist = dist[i][j]

    if min_dist == int(1e9): # 먹을 수 있는 물고기가 없는 경우
        return None
    else:
        return findx , findy , min_dist

# 반복문을 통해서 상어의 움직임 시뮬레이션 시행
res = 0 # 최종 결과
eat = 0 # 먹은 물고기 수

while True:
    tmp = bfs()
    f = find(tmp)

    # 더 이상 먹을 수 있는 물고기가 공간에 없다면 엄마 상어에게 도움을 요청한다.
    if f == None:
        print(res)
        break
    # 물고기를 먹을 수 있는 상황
    else:
        # 먹이를 먹는 곳으로 이동 -> 상어의 현재 위치 변경
        nowx , nowy = f[0] , f[1]
        res += f[2] # find함수를 통해 리턴된 최소 거리가 res값 (상어는 1초에 한칸씩 이동이 가능하기 때문)

        # 상어 위치 변경
        graph[nowx][nowy] = 0 # 상어가 이동하며 물고기를 먹었기 때문에 아무것도 없는 것으로 변경

        # 상어 크기 확인
        eat += 1 # 현재 물고기를 한마리 먹은 상황이므로 상어의 크기 1증가
        # 상어가 먹은 물고기가 현재 사이즈와 같아지면 현재 사이즈 증가
        if eat == now_size:
            now_size += 1
            eat = 0