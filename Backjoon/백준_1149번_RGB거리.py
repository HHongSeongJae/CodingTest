n = int(input())
color = [[]] + [list(map(int,input().split())) for _ in range(n)] # idx를 맞추기 위해서 0번 배열을 만들어둠

dp = [[0] * 3 for _ in range(1001)]

# 처음 시작하는 RGB는 정해져있다.
dp[1][0] = color[1][0]
dp[1][1] = color[1][1]
dp[1][2] = color[1][2]

for i in range(2,n+1):
    # min(dp[i-1][1] , dp[i-1][2]) : 조건에 맞는 인접 색상에서 더 비용이 적은 것 선택
    # color[i][0] : i번째의 색상 선택
    dp[i][0] = min(dp[i-1][1] , dp[i-1][2]) + color[i][0]
    dp[i][1] = min(dp[i-1][0] , dp[i-1][2]) + color[i][1]
    dp[i][2] = min(dp[i-1][0] , dp[i-1][1]) + color[i][2]

print(min(dp[n]))