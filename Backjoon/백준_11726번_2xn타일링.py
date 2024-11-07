n = int(input())

memo = [0] * 1001

# 1 <= n <= 1000
memo[1] = 1
memo[2] = 2

# 점화식
# d[i] = d[i-1] + d[i-2]
for i in range(3, n+1):
    memo[i] = (memo[i-1] + memo[i-2]) % 10007

print(memo[n])