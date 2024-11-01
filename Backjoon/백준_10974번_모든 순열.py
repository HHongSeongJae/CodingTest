# DFS를 이용한 풀이
# n = int(input())
# s = []
# visited = [0] * (n+1)

# def back():
#     # 종료 조건
#     if len(s) == n:
#         print(*s)
#         return
    
#     for i in range(1, n+1):
#         if visited[i] == 0:
#             visited[i] = 1
#             s.append(i)
#             back()
#             visited[i] = 0
#             s.pop()
# back()

## 순열을 이용한 풀이
'''
다음 순열을 찾는 과정을 False가 나올때까지 반복한다.
1. A[i-1] < A[i]를 만족하는 가장 큰 i를 찾는다.
2. j >= i인 A[j] > A[i-1]를 만족하는 가장 큰 j를 찾는다.
3. A[i-1]과 A[j]를 Swap
4. A[i]부터 순열을 뒤집는다.
'''

def next_permutation(a):
    i = len(a) - 1

    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    
    # 마지막 순열까지 진행됨
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
    
    return a

n = int(input())

per = [i for i in range(1, n+1)]
print(' '.join(map(str,per)))

# 마지막 순열(False)가 나올때까지 next_permutation함수를 수행하면된다.
while True:
    per = next_permutation(per)

    if per == False:
        break
    else:
        print(' '.join(map(str,per)))