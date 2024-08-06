## 시간초과 발생
## 거듭 제곱수인 b만큼 a를 곱하는 연산이 수행되기 때문에 O(n)이라는 시간 복잡도를 갖게 된다.

# a,b,c = map(int,input().split())

# print((a**b) % c)

# # 재귀함수 활용 분할정복 알고리즘 적용
import sys

a,b,c = map(int,sys.stdin.readline().split())

def result(a,n):
    if n == 1:
        return a % c
    else:
        x = result(a, n//2)

        if n % 2 == 0:
            return (x * x) % c
        else:
            return (x * x * a) % c

print(result(a,b))