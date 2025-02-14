from collections import deque

# 방향 벡터
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n , k = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

q = []

# 해당 문제는 시작점이 지정되어있지 않다.
# 또한 BFS 탐색이 바이러스의 번호에 따라, 시간에 따라 진행되어야한다.
# 그래서, 바이러스에 대한 정보를 리스트에 우선 넣어준다.
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            q.append((graph[i][j] , 0 , i , j)) # 바이러스 번호 , 시작시간(0으로 시작) , 좌표x, 좌표y

# 바이러스 번호가 낮은 것부터 전염이 시작되므로 바이러스 번호가 낮은 순서대로 정렬
q.sort() # [0]번째 요소를 가지고 정렬하므로 바로 sort를 사용해도 된다.
# q.sort(key=lambda x:x[0])  # lambda 사용식

# BFS탐색을 위하여 큐로 만들어준다.
queue = deque(q)

s , x , y = map(int,input().split())

# BFS 탐색 시작
while queue:
    virus_num , time , xx , yy = queue.popleft()

    # 꺼낸 요소의 시간(time)이 s(종료시간)이라면 BFS 종료
    if s == time:
        break

    # 현재 좌표를 기준으로 상하좌우 확인
    for dir in range(4):
        nx = xx + dx[dir]
        ny = yy + dy[dir]
        
        # graph 범위 내면서 아무런 바이러스가 전이되지 않은 곳에만 바이러가 전이된다.
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
            graph[nx][ny] = virus_num
            queue.append((virus_num , time+1 , nx , ny)) # 여기서 전이된 바이러스는 다음 시간대(s+1)에서 전이가 되므로 time+1로 큐에 넣어준다.

print(graph[x-1][y-1])