n , m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

# 가장자리가 0으로 채워지는 배열 생성
new_graph = [[0] * (m+2)] + [[0] + row + [0] for row in graph] + [[0] * (m+2)]

# 4방면 방향 벡터
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 결과
res = 0

# 위아래
res += (n * m) * 2

for i in range(n+2):
    for j in range(m+2):
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]

            if 0 <= nx < (n+2) and 0 <= ny < (m+2):
                if new_graph[i][j] >= new_graph[nx][ny]:
                    res += abs(new_graph[i][j] - new_graph[nx][ny])

print(res)