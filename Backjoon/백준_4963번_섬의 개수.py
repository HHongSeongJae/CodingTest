import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6) # ★ 이것을 넣어주지 않으면 런타임 에러발생

#방향 : 대각선 포함
dx = [1, -1, 0, 0, 1, -1, 1, -1] 
dy = [0, 0, 1, -1, 1, -1, -1, 1]

def dfs(x,y):
    global count

    # 기준점부터 8가지 방향 확인
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < h) and (0 <= ny < w): #맵의 범위 안
            if graph[nx][ny] == 1: # land를 만나면 sea로 변경한다.
                graph[nx][ny] = 0
                dfs(nx,ny) # dfs 재귀호출

while True:
    w,h = map(int,input().split())

    if w == 0 and h == 0:
        break

    graph = []
    count = 0
    for i in range(h):
        graph.append(list(map(int,input().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1: # land를 만나면 그 지점에서 dfs를 수행
                dfs(i,j)
                count += 1  # dfs가 모두 수행되었다는 것은 연결된 육지를 모두 지나간 것이라서 count + 1 해준다.
    print(count)