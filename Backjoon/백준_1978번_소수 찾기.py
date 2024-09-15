from math import *


def findPrime(n):
    mid = int(sqrt(n))

    # 1은 소수가 아님
    if n < 2:
        return 0

    # 루트(N) 이전까지 소수가 존재하지 않는다면 이 수는 약수
    for i in range(2, mid+1):
        # 나눠지는 수가 존재하면 약수가 아니다.
        if n % i == 0:
            return 0
    
    return 1

N = int(input())

num = list(map(int,input().split()))

count = 0
for i in num:
    if findPrime(i):
        count += 1

print(count)

