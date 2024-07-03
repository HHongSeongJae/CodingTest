'''
3kg
5kg
'''

# 3 혹은 5의 배수가 아니면 -1
# 5로 최대한 봉지를 나누고 나머지는 3kg로 나눈다.

N = int(input())

count = 0

while N > 0:
    #3의 배수면 3을 나눈다
    if N % 5 == 0:
        count += 1
        N = N - 5
    #나머지는 5로 나눈다.
    else:
        count += 1
        N = N - 3

if N == 0:
    print(count)
else:
    print(-1)