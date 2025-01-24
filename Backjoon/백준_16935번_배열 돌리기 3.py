# # 1번 연산 : 상하 반전
# def first(a):
#     n = len(a)
#     m = len(a[0])

#     B = [[0] * m for _ in range(n)]

#     for i in range(n):
#         for j in range(m):
#             B[i][j] = a[n-1-i][j]
    
#     return B

# # 2번 연산 : 좌우 반전
# def second(a):
#     n = len(a)
#     m = len(a[0])

#     B = [[0] * m for _ in range(n)]

#     for i in range(n):
#         for j in range(m):
#             B[i][j] = a[i][m-1-j]
    
#     return B

# # 3번 연산 : 시계방향
# def rotateR(a):
#     n = len(a)
#     m = len(a[0])

#     B = [[0] * n for _ in range(m)]

#     for i in range(m):
#         for j in range(n):
#             B[i][j] = a[n-1-j][i]

#     return B

# # 4번 연산 : 반시계방향
# def rotateL(a):
#     n = len(a)
#     m = len(a[0])

#     B = [[0] * n for _ in range(m)]

#     for i in range(m):
#         for j in range(n):
#             B[i][j] = a[j][m-1-i]

#     return B

# # 5번 연산 : 1->2->3->4
# def five(a):
#     n = len(a)
#     m = len(a[0])

#     B = [[0] * m for _ in range(n)]

#     for i in range(n//2):
#         for j in range(m//2):
#             B[i][j + (m//2)] = a[i][j]
#             B[i + (n//2)][j + (m//2)] = a[i][j + (m//2)]
#             B[i + (n//2)][j] = a[i + (n//2)][j + (m//2)]
#             B[i][j] = a[i + (n//2)][j]

#     return B

# # 6번 연산 : 1->4->3->2
# def six(a):
#     n = len(a)
#     m = len(a[0])

#     B = [[0] * m for _ in range(n)]

#     for i in range(n//2):
#         for j in range(m//2):
#             B[i + (n//2)][j] = a[i][j]
#             B[i + (n//2)][j + (m//2)] = a[i + (n//2)][j]
#             B[i][j + (m//2)] = a[i + (n//2)][j + (m//2)]
#             B[i][j] = a[i][j + (m//2)]

#     return B

# # 기존 배열 A , 연산 수행 후 배열 B
# n, m, r = map(int,input().split())

# A = [list(map(int,input().split())) for _ in range(n)]
# move = list(map(int,input().split()))


# for mm in move:
#     if mm == 1:
#         A = first(A)
#     elif mm == 2:
#         A = second(A)
#     elif mm == 3:
#         A = rotateR(A)
#     elif mm == 4:
#         A = rotateL(A)
#     elif mm == 5:
#         A = five(A)
#     elif mm == 6:
#         A = six(A)

# for i in A:
#     print(*i)

## 재풀이
n,m,r=map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]
move = list(map(int,input().split()))

def one(old):
    # 연속적인 연산을 수행하므로 (3번 혹은 4번 연산)으로 인하여 n과 m이 변할 수 있어 매번 n과 m을 구한다.
    n = len(old)
    m = len(old[0])

    new = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            new[i][j] = old[(n-1) - i][j]

    return new

def two(old):
    # 연속적인 연산을 수행하므로 (3번 혹은 4번 연산)으로 인하여 n과 m이 변할 수 있어 매번 n과 m을 구한다.
    n = len(old)
    m = len(old[0])

    new = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            new[i][j] = old[i][(m-1)-j]
    
    return new

def three(old):
    # 연속적인 연산을 수행하므로 (3번 혹은 4번 연산)으로 인하여 n과 m이 변할 수 있어 매번 n과 m을 구한다.
    n = len(old)
    m = len(old[0])

    new = [[0] * n for _ in range(m)] # 가로세로(n,m)의 크기가 바뀜

    for i in range(n):
        for j in range(m):
            new[j][(n-1)-i] = old[i][j] # 가로세로(n,m)의 크기가 바뀜

    return new

def four(old):
    # 연속적인 연산을 수행하므로 (3번 혹은 4번 연산)으로 인하여 n과 m이 변할 수 있어 매번 n과 m을 구한다.
    n = len(old)
    m = len(old[0])

    new = [[0] * n for _ in range(m)] # 가로세로의 크기가 바뀜

    for i in range(n):
        for j in range(m):
            new[(m-1)-j][i] = old[i][j] # 가로세로(n,m)의 크기가 바뀜

    return new

def five(old):
    # 연속적인 연산을 수행하므로 (3번 혹은 4번 연산)으로 인하여 n과 m이 변할 수 있어 매번 n과 m을 구한다.
    n = len(old)
    m = len(old[0])

    new = [[0] * m for _ in range(n)]

    for i in range(n//2):
        for j in range(m//2):
            new[i][j+(m//2)] = old[i][j] # 1->2
            new[i+(n//2)][j+(m//2)] = old[i][j+(m//2)] # 2-> 3
            new[i+(n//2)][j] = old[i+(n//2)][j+(m//2)] # 3-> 4
            new[i][j] = old[i+(n//2)][j] # 4 -> 1

    return new

def six(old):
    # 연속적인 연산을 수행하므로 (3번 혹은 4번 연산)으로 인하여 n과 m이 변할 수 있어 매번 n과 m을 구한다.
    n = len(old)
    m = len(old[0])

    new = [[0] * m for _ in range(n)]

    for i in range(n//2):
        for j in range(m//2):
            new[i+(n//2)][j] = old[i][j] # 1 -> 4
            new[i][j] = old[i][j+(m//2)] # 2 -> 1
            new[i][j+(m//2)] = old[i+(n//2)][j+(m//2)] # 3 -> 2
            new[i+(n//2)][j+(m//2)] = old[i+(n//2)][j] # 4 -> 3

    return new

for moving in move:
    if moving == 1:
        graph = one(graph)
    elif moving == 2:
        graph = two(graph)
    elif moving == 3:
        graph = three(graph)
    elif moving == 4:
        graph = four(graph)
    elif moving == 5:
        graph = five(graph)
    elif moving == 6:
        graph = six(graph)

for gg in graph:
    print(*gg)