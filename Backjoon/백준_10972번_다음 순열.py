'''
- 다음 순열
[1] A[i-1] < A[i]를 만족하는 가장 큰 i를 찾는다.
[2] j >= i 이면서 A[j] > A[i-1]를 만족하는 가장 큰 j를 찾는다.
[3] A[i-1]과 A[j]를 swap 한다.
[4] A[i]부터 순열을 뒤집는다.

- 만약 순열이 내림차순이라면 마지막 순열이므로 -1을 출력
'''

n = int(input())
A = list(map(int,input().split()))

# [1] A[i-1] < A[i]를 만족하는 가장 큰 i를 찾는다.
idxi = -1
for i in range(n-1 , 0, -1):
    if A[i-1] < A[i]:
        idxi = i
        break

# * 주어진 수열이 마지막 수열이라면 -1 출력
if idxi == -1:
    print(-1)
    exit()

# [2] j >= i 이면서 A[j] > A[i-1]를 만족하는 가장 큰 j를 찾는다.
idxj = n - 1
for i in range(n-1 , 0, -1):
    if A[idxi-1] < A[i]:
        idxj = i
        break

# [3] A[i-1]과 A[j]를 swap 한다.
A[idxi-1] , A[idxj] = A[idxj] , A[idxi-1]

# [4] A[i]부터 순열을 뒤집는다.
final = n - 1

while idxi < final:
    A[idxi] , A[final] = A[final] , A[idxi]
    idxi += 1
    final -= 1

print(' '.join(map(str,A)))