# n,m,k = map(int,input().split()) # n = row , m = col

# graph = [list(map(int,input().split())) for _ in range(n)]
# visited = [[0] * m for _ in range(n)]

# # 상하좌우
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# maxNum = -int(1e9)

# def dfs(px, py, cnt, res):
#     global maxNum

#     if cnt == k:
#         maxNum = max(maxNum , res)
#         return
    
#     for i in range(px , n):
#         for j in range(py if i == px else 0 , m): # px행은 py가 적용되는 행이므로 i == px 이면 py~m이고 나머지는 0~m을 순회하면 된다
#             if visited[i][j] == 0:
#                 ok = 1

#                 for z in range(4):
#                     nx = i + dx[z]
#                     ny = j + dy[z]

#                     if 0 <= nx < n and 0 <= ny < m:
#                         if visited[nx][ny] == 1: # 인접한 칸에 하나라도 선택된 칸이 있다면 false
#                             ok = 0
#                 # 인접한 칸에 선택된 칸이 없다면 해당 칸은 선택 가능
#                 if ok == 1:
#                     visited[i][j] = 1
#                     dfs(i, j, cnt+1, res + graph[i][j])
#                     visited[i][j] = 0

# dfs(0,0,0,0)

# print(maxNum)


## 2차원을 1차원으로 변경

n,m,k = map(int,input().split()) # n = row , m = col

graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

maxNum = -int(1e9)

def dfs(prev, cnt, res):
    global maxNum

    if cnt == k:
        maxNum = max(maxNum , res)
        return
    
    for i in range(prev+1 , n*m):
        x = i // m
        y = i % m

        ok = 1

        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 1:
                    ok = 0
        
        if ok == 1:
            visited[x][y] = 1
            dfs(x*m+y, cnt+1, res+graph[x][y])
            visited[x][y] = 0

dfs(-1,0,0)

print(maxNum)