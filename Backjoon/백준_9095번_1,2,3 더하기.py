# '''
# 숫자 : 개수  : 케이스
# 1    :  1   :  1
# 2    :  2   :  1 1 , 2
# 3    :  4   :  1 1 1 , 1 2 , 2 1 , 3
# 4    :  7   :  1 1 1 1 , 1 1 2 , 1 2 1 , 2 1 1 , 2 2 , 1 3 , 3 1
# 5    :  13  :  1 1 1 1 1 , 1 1 1 2 , 1 1 2 1 , 1 2 1 1 , 2 1 1 1 , 2 2 1 , 2 1 2 , 1 2 2 , 2 3 , 3 2 , 3 1 1 , 1 3 1 , 1 1 3
# '''

# '''
# 규칙
# 4는 1+2+3 = 7개
# 5는 2+3+4 = 13개
#     '
#     '
#     '
# '''

# T = int(input())

# for _ in range(T):
#     # 입력될 n은 1~10
#     dp = [0 for i in range(11)]

#     # 점화식에 따라 1,2,3은 고정
#     dp[1] = 1
#     dp[2] = 2
#     dp[3] = 4

#     n = int(input())

#     for i in range(4, n+1):
#         dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
#     print(dp[n])


## 재풀이
def dfs(cnt , idx , s , n):
    global res

    # 1,2,3을 이용해서 n 숫자를 만든 경우
    if s == n:
        res += 1
        return
    
    # 1,2,3을 이용해서 n 숫자를 만들지 못한 경우
    if s > n:
        return
    
    # 1,2,3을 각각 사용하는 경우를 재귀를 이용하여 모두 찾는다.
    for i in range(1,4):
        dfs(cnt + 1 , i , s + i , n)

t = int(input())

for _ in range(t):
    n = int(input())
    res = 0
    dfs(0,0,0,n)
    print(res)