n = int(input())
tri = [list(map(int,input().split())) for _ in range(n)]

# dp[i][j] : i번째 줄에 j칸에 있는 삼각형의 수
dp = [[0] * (n) for _ in range(n)] 

# 초기화
# 0번째 줄 0번째 칸은 가장 처음 시작되는 삼각형이다.
dp[0][0] = tri[0][0]

for i in range(1,n): # 위에서 초기화한 0번째 제외하고, 1~n-1번째 줄 (리스트 형태이므로 idx에 맞게 n-1까지 수행)
    for j in range(i+1): # 삼각형의 모양을 보면 0~i 까지로 j가 구성된다.
        if j == 0: # 가장 왼쪽에 있는 칸은 우측 상단에서 밖에 경로가 없다.
            dp[i][j] = dp[i-1][j] + tri[i][j]
        elif j == i: # 가장 오른쪽에 있는 칸은 좌측 상단에서 밖에 경로가 없다.
            dp[i][j] = dp[i-1][j-1] + tri[i][j]
        else: # 나머지는 왼쪽, 오른쪽에서 경로가 가능한데 이 중 최대 값의 경로만 선택하면서 아래로 내려가면 된다.
            dp[i][j] = max(dp[i-1][j-1] , dp[i-1][j]) + tri[i][j]

print(max(dp[n-1])) # 가장 마지막 줄에 있는 것 중 max값이 최대값을 유지하는 경로이다.