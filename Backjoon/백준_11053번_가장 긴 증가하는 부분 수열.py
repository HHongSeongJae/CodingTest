## 시간 초과 
## 이유: 해당 방식은 모든 부분 수열을 구하는 방식
## 이유: 해당 숫자를 선택/선택안함의 기준으로 생각하면 2^N 가지의 경우의 수이다.
## 이유: 그러므로 2^1000 이기에 시간초과가 발생한다.

# n = int(input())
# a = list(map(int,input().split()))
# visited = [0] * (len(a))

# res = []

# def dfs(idx, select, visited, length, prev):
#     global res

#     if select == length:
#         res.append(select)
#         return
    
#     for i in range(idx, n):
#         if visited[i] == 0 and prev < a[i]:
#             visited[i] = 1
#             dfs(i , select + 1 , visited , length , a[i])
#             visited[i] = 0

# for l in range(len(a)):
#     dfs(0,0,visited,l,0)

# print(max(res))

#################################################################################
## DP로 풀이해야함
n = int(input())
a = list(map(int,input().split()))

d = [0] * 1001

for i in range(n):
    d[i] = 1 # 자신만 가지는 부분 수열의 길이는 1
    for j in range(i):
        if a[j] < a[i]: # 증가하는 수열 찾음
            tmp = d[i] + 1
            d[i] = max(d[i] , tmp) # 더 긴 길이만 저장

print(max(d))