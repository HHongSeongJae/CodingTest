'''
3kg
5kg
'''

# 3 혹은 5의 배수가 아니면 -1
# 5로 최대한 봉지를 나누고 나머지는 3kg로 나눈다.

# N = int(input())

# count = 0

# while N > 0:
    # #3의 배수면 3을 나눈다
    # if N % 5 == 0:
    #     count += 1
    #     N = N - 5
    # #나머지는 5로 나눈다.
    # else:
    #     count += 1
    #     N = N - 3

# if N == 0:
#     print(count)
# else:
#     print(-1)


## 중간 종료 조건으로 시간 단축 가능
N = int(input())

count = 0
while N > 0:
    # 처음부터 5의 배수이면 5kg 봉지로 담는게 가장 최소의 조건
    if N%5==0:
        count += (N // 5)
        break
    
    # 처음이 5의 배수가 아니면 3kg를 담는다.
    N -= 3
    count += 1

    # 3kg 5kg로 담을 수 없는 상황은 count를 -1로 만든다.
    if N < 0:
        count = -1
    # 다시 한 번 5의 배수이면 한번에 담을 수 있게된다.
    elif N % 5 == 0:
        count += (N//5)
        break

print(count)