mod = 1000000000

n , k = map(int,input().split())

# d[k][n] : k개의 숫자를 사용하여 합 N 만드는 경우의 수
d = [[0] * (n+1) for _ in range(k+1)] 

# 0개의 숫자를 이용하여 합 0을 만드는 경우는 1가지 존재
d[0][0] = 1

for i in range(1,k+1): # 정수 K개 더하기
    for j in range(n+1): # 0 ~ N 사이의 숫자 사용
        for L in range(j+1):
            d[i][j] += d[i-1][j-L]
        d[i][j] %= mod

print(d[k][n])