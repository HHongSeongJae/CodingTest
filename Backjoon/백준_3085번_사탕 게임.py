# 풀이 방법 1
'''
- 연속된 색깔을 검사하는 함수 :: 모든 행과 열을 검사하며 연속적인 색깔이 나오는 최고의 개수를 구한다.
    - O(N^2)

- 서로 교환하기 위한 두 칸을 선택하는 경우 :: 모든 행과 열을 순회함 O(N^2)

=> N^2 x N^2 = N^4  :: O(N^4) 
'''

# N = int(input())
# candy = [list(input()) for _ in range(N)]

# # 연속된 색깔 확인
# def check(a):
#     l = len(a)

#     answer = 1
#     # 행 찾기
#     for i in range(l):
#         cnt = 1
#         for j in range(1,l):
#             if a[i][j] == a[i][j-1]:
#                 cnt += 1
#             else:
#                 cnt = 1
            
#             if answer < cnt:
#                 answer = cnt

#     # 열 찾기
#     for i in range(l):
#         cnt = 1
#         for j in range(1,l):
#             if a[j][i] == a[j-1][i]:
#                 cnt += 1
#             else:
#                 cnt = 1
            
#             if answer < cnt:
#                 answer = cnt
    
#     return answer

# # 인접한 두 카드를 선택하고 교환해본다.
# result = 0
# for i in range(N):
#     for j in range(N):
#         # 현재기준 오른쪽을 선택
#         if j + 1 < N: # N x N 타일을 벗어나지 않을 경우에만 실행
#             # 선택한 인접타일을 교환시켜본다.
#             candy[i][j], candy[i][j+1] = candy[i][j+1] , candy[i][j]
#             t = check(candy)

#             # 가장 많이 인접한 케이스
#             if t > result:
#                 result = t

#             # 원상 복구
#             candy[i][j], candy[i][j+1] = candy[i][j+1] , candy[i][j]

#         # 현재기준 아래쪽을 선택
#         if i + 1 < N: # N x N 타일을 벗어나지 않을 경우에만 실행
#             # 선택한 인접타일을 교환시켜본다.
#             candy[i][j], candy[i+1][j] = candy[i+1][j] , candy[i][j]
#             t = check(candy)

#             # 가장 많이 인접한 케이스
#             if t > result:
#                 result = t

#             # 원상 복구
#             candy[i][j], candy[i+1][j] = candy[i+1][j] , candy[i][j]

# print(result)

# 풀이 방법 2
'''
- 연속된 색깔을 검사하는 함수 :: 모든 행과 열을 검사하며 연속적인 색깔이 나오는 최고의 개수를 구한다.
    - O(N^2)

- 교환이 이뤄진 행과 열만 검사한다(3개의 행 혹은 열이 될 것임) => 3 x N => O(N)

=> N^2 x N = N^3  :: O(N^3) 
'''

N = int(input())

candy = [list(input()) for _ in range(N)]

def check(a, startRow, endRow, startCol, endCol):
    l = len(a)
    answer = 1
    
    # 행 검사
    for i in range(startRow , endRow+1):
        cnt = 1
        for j in range(1,l):
            if a[i][j] == a[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            
            if answer < cnt:
                answer = cnt
    
    # 열 검사
    for i in range(startCol , endCol+1):
        cnt = 1
        for j in range(1,l):
            if a[j][i] == a[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            
            if answer < cnt:
                answer = cnt

    return answer

res = 1
for i in range(N):
    for j in range(N):
        # 우측 인접한 것
        if j + 1 < N: # 유효한 범위
            candy[i][j] , candy[i][j+1] = candy[i][j+1] , candy[i][j]
            temp = check(candy , i , i , j , j + 1)
            candy[i][j] , candy[i][j+1] = candy[i][j+1] , candy[i][j] # 원상복구

            if res < temp:
                res = temp

        # 아래와 인접한 것
        if i + 1 < N:
            candy[i][j] , candy[i+1][j] = candy[i+1][j] , candy[i][j]
            temp = check(candy , i , i+1 , j , j)
            candy[i][j] , candy[i+1][j] = candy[i+1][j] , candy[i][j] # 원상복구

            if res < temp:
                res = temp

print(res)