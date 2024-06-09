K = int(input())

for _ in range(K):
    k = int(input())
    n = int(input())

    # DP 테이블
    d = [[i for i in range(n+1)] for j in range(k+1)]

    for i in range(1, k+1):
        d[i][0] = 0
        d[i][1] = 1

        for j in range(1, n+1):
            d[i][j] = d[i-1][j] + d[i][j-1]

    print(d[k][n])