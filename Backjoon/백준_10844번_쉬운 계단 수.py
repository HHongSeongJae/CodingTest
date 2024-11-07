mod = 1000000000

n = int(input())

d = [[0] * 10 for _ in range(101)]

for i in range(1,n+1): # 숫자의 길이
    for j in range(10): # 사용하는 수
        # 길이가 1이면 1~9까지는 경우의 수가 1가지 뿐이다.
        if i == 1 and j != 0:
            d[i][j] = 1
            continue
        
        # j = 0이면 -1은 될 수 없기 때문에 j+1 경우만 가능하다.
        if j == 0:
            d[i][j] += d[i-1][j+1]
        elif j == 9: # j=9 이면 10이 될 수 없기 때문에 j-1 경우만 가능하다.
            d[i][j] += d[i-1][j-1]
        else: # 그 외의 경우에는 j-1 , j+1의 경우가 가능하다.
            d[i][j] += d[i-1][j-1]
            d[i][j] += d[i-1][j+1]

        d[i][j] %= mod

print(sum(d[n]) % mod)