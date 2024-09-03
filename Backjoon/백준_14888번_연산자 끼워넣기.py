'''
* 연산자 우선순위는 무시
* 수의 순서는 변경 금지
* 나눗셈은 몫만 고려

- 식의 결과 : 최대 , 최소
- [+ , - , * , /]
'''

import sys

input = sys.stdin.readline

N = int(input())
num = list(map(int,input().split()))
operation = list(map(int,input().split())) # 연산자 : + - * //

maxTemp = -int(1e9)
minTemp = int(1e9)

def dfs(depth , n):
    global maxTemp , minTemp

    # 종료 조건
    if depth == (N-1):
        maxTemp = max(maxTemp , n)
        minTemp = min(minTemp , n)
        return

    # 더하기
    if operation[0] != 0:
        operation[0] -= 1
        dfs(depth + 1 , n + num[depth + 1])
        operation[0] += 1
    
    # 빼기
    if operation[1] != 0:
        operation[1] -= 1
        dfs(depth + 1 , n - num[depth + 1])
        operation[1] += 1
    
    # 곱하기
    if operation[2] != 0:
        operation[2] -= 1
        dfs(depth + 1 , n * num[depth + 1])
        operation[2] += 1
    
    # 나누기
    if operation[3] != 0:
        operation[3] -= 1
        dfs(depth + 1 , int(n / num[depth+1]))  # (-1) // 3 == -1 결과가 나오므로 int(n/num[depth+1])로 표현
        operation[3] += 1

dfs(0, num[0])

print(maxTemp)
print(minTemp)
