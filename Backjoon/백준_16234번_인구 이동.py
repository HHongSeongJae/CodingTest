'''
* 인구이동이 없을 때까지 아래의 동작을 수행한다.
- bfs 수행한다.
    - BFS로 4방향을 확인
    - 인구 차이가 L <= <= R 이면
        - cnt += 1
        - temp리스트에 해당 좌표 저장
        - BFS 큐에 리스트 저장
    - BFS 탐색이 종료되면 temp에 저장된 좌표의 값들을 모두 더한다.
    - (모두더한값) // (cnt) => temp 좌표들에 모두 적용 (temp.popleft())
'''

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,l,r = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

# BFS 탐색
def bfs(x,y,cnt):
    q = deque()
    q.append((x,y))

    # 연합을 만들 수 있는 구역의 좌표 저장
    temp = set() 
    temp.add((x,y))

    visited[x][y] = cnt

    sum = graph[x][y] # 총합
    count = 1 # 엽합 개수

    while q:
        xx , yy = q.popleft()

        for dir in range(4):
            nx = xx + dx[dir]
            ny = yy + dy[dir]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if l <= abs(graph[xx][yy] - graph[nx][ny]) <= r:
                    q.append((nx,ny))
                    temp.add((nx,ny))
                    visited[nx][ny] = cnt

                    sum += graph[nx][ny] # 연합의 값 추가
                    count += 1 # 연합 개수 추가
    
    # 연합을 이루는 칸의 값 갱신
    for cx , cy in temp:
        graph[cx][cy] = sum // count

# 연합이 생길 수 없을 상황까지 반복하며 BFS 확인
res = 0

while True:
    visited = [[-1] * n for _ in range(n)]
    check = 0 # 인구이동이 더 이상 발생하지 않는지 확인하기 위한 것

    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                bfs(i,j,check)
                check += 1
    
    # 모든 graph를 순회했을 때 check가 n*n 값이라면 모든 위치에서의 인구이동이 불가한 상황이 된 것
    if check == n*n:
        break # 종료

    # 위 상황이 아니면 한 번더 반복하므로 개수 추가
    res += 1

print(res)