# # Python 집합 자료형을 사용한 방식
# import sys

# input = sys.stdin.readline

# T = int(input())

# S = set()
# for _ in range(T):
#     a , *b = input().split()

#     if len(b) > 0:
#         x = int(b[0])

#     # add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
#     # set 자료형은 중복을 허용하지 않음으로 별도의 조건 필요없이 이미 있는 경우에는 연산이 무시된다.
#     if a == 'add':
#         S.add(x)
    
#     # remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
#     if a == 'remove':
#         if x in S: # x가 S에 있을 경우에만 제거 수행
#             S.remove(x)

#     # check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
#     if a == 'check':
#         if x in S: # S가 x에 있다면 1 출력
#             print(1)
#         else: # S가 x에 있다면 0 출력
#             print(0)
    
#     # toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
#     if a == 'toggle':
#         if x in S: # S가 x에 있다면 x 제거
#             S.remove(x)
#         else: # S가 x에 있다면 x 추가
#             S.add(x)
    
#     # all: S를 {1, 2, ..., 20} 으로 바꾼다.
#     if a == 'all':
#         # S를 새롭게 정의한 후 1~20을 추가한다.
#         S = set()
#         for i in range(1,21):
#             S.add(i)
    
#     # empty: S를 공집합으로 바꾼다.
#     if a == 'empty':
#         S = set() # S 초기화


## 비트마스크 이용
## 1<= x <= 20 이기 때문에 비트마스크를 사용할 수 있다.
# Python 집합 자료형을 사용한 방식
import sys

input = sys.stdin.readline
n = 20

T = int(input())

S = 0
for _ in range(T):
    a , *b = input().split()

    if len(b) > 0:
        x = int(b[0]) - 1

    # add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
    # set 자료형은 중복을 허용하지 않음으로 별도의 조건 필요없이 이미 있는 경우에는 연산이 무시된다.
    if a == 'add':
        S = (S | (1 << x))
    # remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
    elif a == 'remove':
        S = (S & ~(1 << x))
    # check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
    elif a == 'check':
        res = (S & (1 << x))
        if res > 0:
            print(1)
        else:
            print(0)
    # toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
    elif a == 'toggle':
        S = (S ^ (1 << x))
    # all: S를 {1, 2, ..., 20} 으로 바꾼다.
    elif a == 'all':
        S = (1 << n) - 1
    # empty: S를 공집합으로 바꾼다.
    else:
        S = 0