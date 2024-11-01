'''
- 이전 순열
[1] A[i-1] > A[i]를 만족하는 가장 큰 i를 찾는다.
[2] j >= i 이면서 A[j] < A[i-1]를 만족하는 가장 큰 j를 찾는다.
[3] A[i-1]과 A[j]를 swap 한다.
[4] A[i]부터 순열을 뒤집는다.
'''

def prev_permutation(a):
    # [1] A[i-1] > A[i]를 만족하는 가장 큰 i를 찾는다.
    i = len(a) - 1

    while i > 0 and a[i-1] <= a[i]:
        i -= 1
    
    # 가장 처음에 오는 순열
    if i <= 0:
        return False
    
    # [2] j >= i 이면서 A[j] < A[i-1]를 만족하는 가장 큰 j를 찾는다.
    j = len(a) - 1
    
    while a[j] >= a[i-1]:
        j -= 1
    
    # [3] A[i-1]과 A[j]를 swap 한다.
    a[i-1] , a[j] = a[j] , a[i-1]

    # [4] A[i]부터 순열을 뒤집는다.
    j = len(a) - 1
    while i < j:
        a[i] , a[j] = a[j], a[i]
        i += 1
        j -= 1

    return a

n = int(input())
per = list(map(int,input().split()))

res = prev_permutation(per)
if res == False:
    print(-1)
else:
    print(' '.join(map(str,res)))