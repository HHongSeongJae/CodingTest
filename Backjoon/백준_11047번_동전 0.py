"""
구현
1. 리스트 내림 차순 정렬
2. 큰 것부터 // 연산 (가능하면 연산 후 개수 카운트 후 %로 남은 가격)
"""
import sys

input = sys.stdin.readline

n , k = map(int,input().split())

# 보유한 동전
money = []
for _ in range(n):
    money.append(int(input()))

# 1. 받은 리스트 내림차순
money.sort(reverse=True)

count = 0
for i in money:
    # 동전보다 만들어야 하는 금액이 커야 한다.
    if k >= i:
        count += (k // i)
        k = k % i

print(count)