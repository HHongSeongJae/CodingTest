# 일반적인 방법으로 소수 구하기
# def is_Prime(n):
#     if n < 2:
#         return 0
    
#     i = 2
#     while i*i <= n:
#         if n % i == 0:
#             return 0

#         i += 1
    
#     return 1

# M , N = map(int,input().split())

# for i in range(M, N+1):
#     if is_Prime(i):
#         print(i)

## 에라토스테네스체 구현
MAXNUM = 1000000
check = [0] * (MAXNUM+1) # 수를 지웠으면 1 안지웠으면 0

def is_Prime():    
    # 0 , 1은 소수가 아니기에 바로 지운 것으로 한다.
    check[0] = 1
    check[1] = 1

    # 에라토스테네스체 구현
    for i in range(2, MAXNUM+1):
        # 선택된 소수의 배수를 지운다. (소수의 배수는 소수가 아니기 때문)
        if check[i] == 0: # 지워지지 않은 수 중에서 가장 작은 수 :: 이것이 소수가 된다.
            j = i * i # 이전의 수에서 배수들을 모두 지우기 때문에 i * i 부터 배수를 지워나가면 된다.

            while j <= MAXNUM:
                if check[j] == 0:
                    check[j] = 1
                
                j += i # i의 배수를 모두 순회한다.

M , N = map(int,input().split())

is_Prime()

for i in range(M,N+1):
    # M~N 사이의 숫자중 에라토스테네스 배열에서 지워지지 않은 수가 소수가 된다.
    if check[i] == 0:
        print(i)


