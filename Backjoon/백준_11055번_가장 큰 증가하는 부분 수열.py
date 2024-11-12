n = int(input())
a = [[]] + list(map(int,input().split()))

dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = a[i]

    for j in range(1,i): # j : 1~i-1
        if a[j] < a[i]: # 증가 수열을 찾았다.
            dp[i] = max(dp[i] , dp[j] + a[i]) # 가장 큰 증가하는 수열을 찾는 과정

print(max(dp))