# 오답
# 가장 빠르게 작아지게 하기 위해서 3나누기 -> 2나누기 -> 1빼기 순서로 답을 구해갔다.
# 반례 : 10
    # 위와 같은 방식 사용시 : 10 -> 5 -> 4 -> 2 -> 1
    # 실제로 최소 방식 : 10 -> 9 -> 3 -> 1
    # 이와 같은 반례가 존재하여 오답

# n = int(input())
# res = 0
# memo = [0] * 1000000
# # memo[n] = memo[n % 3]

# def cal(n):
#     global res

#     if n == 1:
#         print(memo[n])
#         return
#     else:
#         if memo[n] > 0:
#             return memo[n]

#         res += 1
#         if n % 3 == 0:
#             print(f'n%3 :: n={n} , memo[n] = {memo[n]}')
#             memo[n] = cal(n//3)
#             return memo[n]
#         elif n % 2 == 0:
#             print(f'n%2 :: n={n} , memo[n] = {memo[n]}')
#             memo[n] = cal(n//2)
#             return memo[n]
#         else:
#             print(f'n- 1:: n={n} , memo[n] = {memo[n]}')
#             memo[n] = cal(n-1)
#             return memo[n]
        
# cal(n)

## Top Down 풀이
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
# 이 문장을 바탕으로 점화식을 구성하면 아래와 같다.
# D[n] = min(D[n//3] , D[n//2] , D[n-1]) + 1


# Python 언어의 특성상 메모리 깊이가 매우 작고, 재귀를 사용하면 매우 시간이 오래걸린다. -> 그래서 Python은 웬만하면 Bottom Up을 사용하는 것이 좋다.
# import sys

# sys.setrecursionlimit(10000000) # Python에서는 재귀에 대한 제한을 걸어주어야 한다.

# n = int(input())
# res = 0
# memo = [0] * (n+1)

# def cal(n):
#     if n == 1:
#         return 0
    
#     # memoization
#     if memo[n] > 0:
#         return memo[n]
    

#     # 점화식 : D[n] = min(D[n//3] , D[n//2] , D[n-1]) + 1
#     # 그런데 min을 위해서 비교하기 위해서는 값이 존재해야한다.
#     # n//3과 n//2는 나누어지는 경우에만 연산이 되기 때문에 모든 경우에 연산이 가능한 n-1부터 수행을 한다.
#     # 그리고 이후의 n//2 , n//3의 조건이 된다면 연산을 수행하여 최소의 값만 memo[n]에 저장한다.
#     memo[n] = cal(n-1) + 1
#     if (n%2 == 0):
#         tmp = cal(n//2) + 1
#         memo[n] = min(memo[n] , tmp)
    
#     if (n%3 == 0):
#         tmp = cal(n//3) + 1
#         memo[n] = min(memo[n] , tmp)
    
#     return memo[n]

# print(cal(n))

## Bottom Up 풀이
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
# 이 문장을 바탕으로 점화식을 구성하면 아래와 같다.
# D[n] = min(D[n//3] , D[n//2] , D[n-1]) + 1

n = int(input())
memo = [0] * (n+1)

# d[1] = 0  :: 가장 마지막값 .. bottom up에서는 이것이 시작값이 된다.
memo[1] = 0

for i in range(2, n+1):
    memo[i] = memo[i-1] + 1 # Top Down과 달리 Bottom Up은 가장 아래에서 올라가기 때문에 memo에 이전 값이 반드시 존재한다.

    if (i % 3) == 0:
        tmp = memo[i//3] + 1
        memo[i] = min(memo[i] , tmp)
    
    if (i % 2) == 0:
        tmp = memo[i//2] + 1
        memo[i] = min(memo[i] , tmp)

print(memo[n])