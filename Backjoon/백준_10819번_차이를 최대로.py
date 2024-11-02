## 순열 직접 구현
# def sumation(a):
#     res = 0

#     for i in range(1,len(a)):
#         res += abs(a[i-1] - a[i])
    
#     return res

# def find_permutation(p):
#     i = len(p) - 1

#     # 1. A[i-1] < A[i]인 가장 큰 i 찾기
#     while i > 0 and p[i-1] >= p[i]:
#         i -= 1
    
#     # 다음 순열이 없는 경우 = 현재 순열이 마지막 순열
#     if i <= 0:
#         return False
    
#     # 2. A[j] > A[i-1]인 j 찾기
#     j = len(p) - 1
#     while p[j] <= p[i-1]:
#         j -= 1
    
#     # 3. swap
#     p[i-1] , p[j] = p[j] , p[i-1]

#     # 4. A[i]위치 부터 뒤집기
#     j = len(p) - 1
#     while i < j:
#         p[i] , p[j] = p[j] , p[i]
#         i += 1
#         j -= 1
    
#     return p

# n = int(input())
# A = list(map(int,input().split()))
# A.sort()

# res = sumation(A)

# # 전체 순열 찾으며 모든 결과 구하기
# while True:
#     A = find_permutation(A)
    
#     # 마지막 순열이 나오면 종료
#     if A == False:
#         break

#     res = max(res, sumation(A))

# print(res)

## permutation 라이브러리 활용
from itertools import permutations

n = int(input())
A = list(map(int,input().split()))

per = list(permutations(A))

def sumation(a):
    res = 0

    for i in range(1,len(a)):
        res += abs(a[i-1] - a[i])
    
    return res

maxSum = 0
for p in per:
    maxSum = max(maxSum , sumation(p))

print(maxSum)