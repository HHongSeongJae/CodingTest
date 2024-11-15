# 1번 연산 : 상하 반전
def first(a):
    n = len(a)
    m = len(a[0])

    B = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            B[i][j] = a[n-1-i][j]
    
    return B

# 2번 연산 : 좌우 반전
def second(a):
    n = len(a)
    m = len(a[0])

    B = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            B[i][j] = a[i][m-1-j]
    
    return B

# 3번 연산 : 시계방향
def rotateR(a):
    n = len(a)
    m = len(a[0])

    B = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            B[i][j] = a[n-1-j][i]

    return B

# 4번 연산 : 반시계방향
def rotateL(a):
    n = len(a)
    m = len(a[0])

    B = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            B[i][j] = a[j][m-1-i]

    return B

# 5번 연산 : 1->2->3->4
def five(a):
    n = len(a)
    m = len(a[0])

    B = [[0] * m for _ in range(n)]

    for i in range(n//2):
        for j in range(m//2):
            B[i][j + (m//2)] = a[i][j]
            B[i + (n//2)][j + (m//2)] = a[i][j + (m//2)]
            B[i + (n//2)][j] = a[i + (n//2)][j + (m//2)]
            B[i][j] = a[i + (n//2)][j]

    return B

# 6번 연산 : 1->4->3->2
def six(a):
    n = len(a)
    m = len(a[0])

    B = [[0] * m for _ in range(n)]

    for i in range(n//2):
        for j in range(m//2):
            B[i + (n//2)][j] = a[i][j]
            B[i + (n//2)][j + (m//2)] = a[i + (n//2)][j]
            B[i][j + (m//2)] = a[i + (n//2)][j + (m//2)]
            B[i][j] = a[i][j + (m//2)]

    return B

# 기존 배열 A , 연산 수행 후 배열 B
n, m, r = map(int,input().split())

A = [list(map(int,input().split())) for _ in range(n)]
move = list(map(int,input().split()))


for mm in move:
    if mm == 1:
        A = first(A)
    elif mm == 2:
        A = second(A)
    elif mm == 3:
        A = rotateR(A)
    elif mm == 4:
        A = rotateL(A)
    elif mm == 5:
        A = five(A)
    elif mm == 6:
        A = six(A)

for i in A:
    print(*i)