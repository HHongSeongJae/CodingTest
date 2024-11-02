# # DFS를 이용하여 순열을 구하여 값을 구하는 풀이 => 시간 초과
# per = []

# def dfs(idx, select , vistied, n , s):
#     global per
#     if select == n:
#         per.append(s)
#         return

#     for i in range(n):
#         if vistied[i] == 0:
#             vistied[i] = 1
#             dfs(i , select + 1 ,vistied , n , s + str(i))
#             vistied[i] = 0

# def sumation(a , map):
#     minSum = int(1e9)
#     for i in a: # a는 모든 순열이 저장된 리스트
#         idx = 0
#         sum = 0

#         for j in range(1,len(i)):
#             row = i[j - 1]
#             col = i[j]
#             sum += map[int(row)][int(col)]

#         sum += map[int(i[-1])][int(i[0])] # 처음으로 다시 돌아오는 경로 추가
#         minSum = min(minSum , sum)
    
#     return minSum

# n = int(input())
# graph = [list(map(int,input().split())) for _ in range(n)]

# visited = [0] * n
# dfs(0, 0 , visited , n , '')

# print(sumation(per, graph))

# '''
# [시간복잡도]
# DFS함수
# - n개의 수로 구성된 순열을 구성하는 함수
# - n! 번 재귀호출

# 합산 함수
# - 모든 순열의 개수 n개

# ==> O(N! x N)
# '''

## 순열 구현으로 풀이
# def next_permuation(a): # 여기서의 파라미터인 a는 next_permutation에서 직접변경하기 때문에 main함수의 d 리스트에 직접 반영된다.
#     i = len(a) - 1

#     while i > 0 and a[i-1] >= a[i]:
#         i -= 1
    
#     if i <= 0:
#         return False
    
#     j = len(a) - 1

#     while a[j] <= a[i-1]:
#         j -= 1

#     a[i-1] , a[j] = a[j] , a[i-1]

#     j = len(a) - 1
#     while i < j:
#         a[i] , a[j] = a[j] , a[i]
#         i += 1
#         j -= 1
    
#     return True

# n = int(input())
# graph = [list(map(int,input().split())) for _ in range(n)]
# d = [i for i in range(n)]

# minSum = int(1e9)
# while True:
#     ok = True # [i][j] 경로가 존재하는지 확인
#     res = 0

#     for i in range(0,n-1):
#         if graph[d[i]][d[i+1]] == 0: # 경로 존재 x :: 경로값을 구하지 않는다.
#             ok = False
#             break
#         else:
#             res += graph[d[i]][d[i+1]]
    
#     # ok == True : 경로가 존재함
#     # graph[d[-1]][d[0]] != 0 : 해당 경로도 존재
#     if ok and graph[d[-1]][d[0]] != 0:
#         res += graph[d[-1]][d[0]]
#         minSum = min(minSum , res) # 최소 비용 구하기

#     # 이 과정에서 다음 순열이 구해진다.
#     if next_permuation(d) == False:
#         break

# print(minSum)


## 개선
def next_permuation(a): # 여기서의 파라미터인 a는 next_permutation에서 직접변경하기 때문에 main함수의 d 리스트에 직접 반영된다.
    i = len(a) - 1

    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    
    if i <= 0:
        return False
    
    j = len(a) - 1

    while a[j] <= a[i-1]:
        j -= 1

    a[i-1] , a[j] = a[j] , a[i-1]

    j = len(a) - 1
    while i < j:
        a[i] , a[j] = a[j] , a[i]
        i += 1
        j -= 1
    
    return True

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
d = [i for i in range(n)]

minSum = int(1e9)
while True:
    ok = True # [i][j] 경로가 존재하는지 확인
    res = 0

    for i in range(0,n-1):
        if graph[d[i]][d[i+1]] == 0: # 경로 존재 x :: 경로값을 구하지 않는다.
            ok = False
            break
        else:
            res += graph[d[i]][d[i+1]]
    
    # ok == True : 경로가 존재함
    # graph[d[-1]][d[0]] != 0 : 해당 경로도 존재
    if ok and graph[d[-1]][d[0]] != 0:
        res += graph[d[-1]][d[0]]
        minSum = min(minSum , res) # 최소 비용 구하기

    # 이 과정에서 다음 순열이 구해진다.
    if next_permuation(d) == False:
        break

    # 0123 , 1230 2301 3012와 같은 순열은 모두 0->1->2->3->0 인 동일한 경로를 의미한다.
    # 그래서 불필요한 계산을 방지하기 위해서 시작점을 고정할 것이다.
    # 1이라는 도시를 시작점으로 고정하기 때문에 d순열의 시작점(d[0])이 0(1번 도시)가 아니라면 더 이상 연산할 의미가 없어진다.
    # d 순열의 시작점이 1이 아니면 종료한다.
    if d[0] != 0:
        break

print(minSum)
