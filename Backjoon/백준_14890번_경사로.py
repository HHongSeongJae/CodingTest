# ################################################################################################
# '''
# 1. 높이가 다른 땅을 만나면 경사로를 둘 수 있는지 확인
#     1-1. 만약 차이가 1이상 나면 False
#     1-2. 차이가 1이라면 경사로가 가능한지 확인
#         #증가하는 상황
#         ## a[i-1] = 1 , a[i] = 2 가 된다면 i-1 부터 거꾸로 L길이 만큼 경사로를 둘 수 있는지를 확인해야 함
#         ## 그래서, i-1 위치부터 i-j가 되어야하고, 거꾸로 가면 인덱스가 0까지 존재하기 때문에 1 <= j <= n이 된다.
#         1 <= j <= N 반복
#             1-1-1. 인덱스가 0보다 작아지면 안되기 때문에 i<j 조건 만족해야함
#             1-1-2. a[i-1] != a[i-j] 이면 경사로를 놓을 수 없다.
#             1-1-3. (1-1-2)가 가능하지만 이미 경사로를 놓았다면 불가능

#         #감소하는 상황
#         ## a[i-1] = 2 , a[i] = 1 가 된다면 i부터 N-1까지 L길이 만큼 경사로를 둘 수 있는지 확인해야 함
#         ## 그래서, i부터 i+j가 되고, 리스트는 0부터 시작함으로 N-1까지 존해하기 때문에 0 <= j < N이 된다.
#         0 <= j < N 반복
#             1-1-1. 인덱스가 N을 초과하면 안된다.
#             1-1-2. a[i] != a[i+j] 이면 경사로를 놓을 수 없다.
#             1-1-3. (1-1-2)가 가능하지만 이미 경사로를 놓았다면 불가능
# # '''
# n , L = map(int,input().split())
# graph = [list(map(int,input().split())) for _ in range(n)]

# # 경사로 확인 함수
# def check(d, L):
#     visited = [0] * n # 경사로를 놓았는지 확인
    
#     for i in range(1,n):
#         if d[i-1] != d[i]:
#             diff = abs(d[i-1] - d[i])
            
#             # 1-1. 만약 차이가 1이상 나면 False
#             if diff != 1:
#                 return False
            
#             # 증가 상황
#             ## a[i-1] = 1 , a[i] = 2 가 된다면 i-1 부터 거꾸로 L길이 만큼 경사로를 둘 수 있는지를 확인해야 함
#             ## 그래서, i-1 위치부터 i-j가 되어야하고, 거꾸로 가면 인덱스가 0까지 존재하기 때문에 1 <= j <= n이 된다.
#             if d[i-1] < d[i]:
#                 for j in range(1,L+1):
#                     if i < j: # 인덱스가 0보다 작아지면 안되기 때문에 i<j 조건 만족해야함
#                         return False
                    
#                     if d[i-1] != d[i-j]: # a[i-1] != a[i-j] 이면 경사로를 놓을 수 없다.
#                         return False
                    
#                     if visited[i-j] == 1: # 이미 경사로를 놓았다면 불가능
#                         return False

#                     visited[i-j] = 1 # 위 조건이 통과 되면 경사로를 놓을 수 있는 상황
#             # 감소 상황
#             ## a[i-1] = 2 , a[i] = 1 가 된다면 i부터 N-1까지 L길이 만큼 경사로를 둘 수 있는지 확인해야 함
#             ## 그래서, i부터 i+j가 되고, 리스트는 0부터 시작함으로 N-1까지 존해하기 때문에 0 <= j < N이 된다.
#             else:
#                 for j in range(L):
#                     if i+j >= n: # 인덱스가 N을 초과하면 안된다.
#                         return False
                    
#                     if d[i] != d[i+j]: # a[i] != a[i+j] 이면 경사로를 놓을 수 없다.
#                         return False
                    
#                     if visited[i+j]: # 이미 경사로를 놓았다면 불가능
#                         return False
                    
#                     visited[i+j] = 1 # 위 조건이 통과 되면 경사로를 놓을 수 있는 상황
#     return True

# res = 0
# # 행 확인
# for row in range(n):
#     d = graph[row]
    
#     if check(d , L) == True:
#         res += 1

# # 열 확인
# for col in range(n):
#     d = [graph[row][col] for row in range(n)]
    
#     if check(d , L) == True:
#         res += 1
        
# print(res)

########################
'''
- 경사로 조건
  - 경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다.
  - 낮은 칸과 높은 칸의 높이차이는 1
  - 경사로를 놓을 수 있는 칸의 높이는 모두 같고 L개의 칸이 연속되어야 함

- 확인
  - 행 방향
  - 열 방향
'''

# 경사로 확인하는 함수
def check(line , l):  # line : 행 / 열 한줄 리스트 , l : 경사로 바닥면의 길이
    visited = [0] * n # 경사로를 놓은 바닥

    for i in range(1, n):
        if line[i-1] != line[i]:
            diff = abs(line[i-1] - line[i])

            if diff != 1: # 높이 차이가 1이상이면 불가능
                return False

            if line[i-1] < line[i]: # 경사가 증가하는 경우
                # i-1 위치부터 L 길이 만큼 확인하여 경사로를 놓을 수 있는지 확인한다.
                for j in range(1,l+1):
                    # 경계 조건 : i - j > 0
                    if 0 <= (i - j) < n:
                        if line[i-j] != line[i-1]:
                            return False
                        
                        # 경사로는 놓을 수 있지만 이미 경사로가 놓여있으면 불가능
                        if visited[i-j] == 1:
                            return False
                            
                        # 경사로 놓을 수 있음
                        visited[i-j] = 1
                    else:
                        return False # 경계 조건이 맞지 않는 경우 False로 리턴하지 않으면 반복문이 계속 수행되어 다른 결과가 나온게 된다.
            else: # 경사가 감소하는 경우
                # i+1 위치부터 L 길이 만큼 확인하여 경사로를 놓을 수 있는지 확인한다.
                for j in range(l):
                    # 경계 조건 : i + j < n
                    if 0 <= (i + j) < n:
                        if line[i+j] != line[i]:
                            return False
                            
                        # 경사로를 놓을 수 있지만 이미 경사로가 놓여있으면 불가능
                        if visited[i+j] == 1:
                            return False
                            
                        # 경사로 놓을 수 있음
                        visited[i+j] = 1
                    else:
                        return False # 경계 조건이 맞지 않는 경우 False로 리턴하지 않으면 반복문이 계속 수행되어 다른 결과가 나온게 된다.

    # 반복문이 정상적으로 종료된다면 경사로를 놓을 수 있는 경우
    # print(f'true point = {line}')
    return True

# 메인
n , l = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

result = 0
# 행 방향 확인
# print("check row")
for i in range(n):
    # 행 방향 추출
    d = graph[i]

    if check(d , l): # 한 행 확인 결과 true가 나오면 지나갈 수 있는 길이다.
        result += 1

# 열 방향 확인
# print("check col")
for i in range(n):
    # 열방향 추출
    d = [graph[j][i] for j in range(n)]

    if check(d , l): # 한 행 확인 결과 true가 나오면 지나갈 수 있는 길이다.
        result += 1

print(result)