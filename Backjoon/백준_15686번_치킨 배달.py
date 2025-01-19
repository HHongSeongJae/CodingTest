n , m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

# 집 리스트와 치킨 리스트 구분
home = []
chicken = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append((i,j))
        elif graph[i][j] == 2:
            chicken.append((i,j))

# 선택한 치킨 집 기록하는 리스트
visited = [0] * len(chicken)

# DFS를 통해 치킨집 선택
def dfs(depth , cnt , graph , visited):
    global res

    # m개의 치킨집이 선택된 경우
    # 치킨 거리 계산
    if cnt == m:
        ans = 0 # 도시의 치킨 거리 계산

        # 집 별로 치킨 거리를 계산하고 가장 짧은 치킨 거리만 반영한다.
        for h in home:
            dist = int(1e9)
            for i in range(len(chicken)):
                if visited[i] == 1: # 선택된 치킨집만 확인
                    # 치킨 거리 계산
                    tmp = abs(h[0] - chicken[i][0]) + abs(h[1] - chicken[i][1])
                    dist = min(dist, tmp)
            ans += dist # 하나의 집에 대한 최소의 치킨거리만 반영
        
        # 도시의 치킨 거리에서 가장 작은 값을 원하기 때문에 이전에 있던 최종적인 결과도 최소값만 반영한다.
        res = min(res,ans)
        return

    # 치킨집 선택
    for i in range(depth , len(chicken)): # 중복 없는 조합선택이므로 depth부터 시작한다.
        if visited[i] == 0:
            visited[i] = 1
            dfs(i+1 , cnt+1 , graph , visited)
            visited[i] = 0

#도시의 가장 작은 치킨거리 값
res = int(1e9)
dfs(0,0,graph,visited)

print(res)