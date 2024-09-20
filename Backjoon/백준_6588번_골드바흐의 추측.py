import sys

input = sys.stdin.readline

MAXNUM = 1000000 # 100만 이하 수까지만 검증

check = [0] * (MAXNUM+1) # 에라토스테네스체 활용해서 소수를 찾기 위한 리스트
prime = []
#소수 연산
def is_Prime():
    # 0,1은 소수가 아니다.
    check[0] = 1
    check[1] = 1

    for i in range(2, MAXNUM+1):
        if check[i] == 0: # 지워지지 않은 수 :: 소수이다.
            prime.append(i) # 소수 저장
            j = i * i

            # 소수의 배수 지우기
            while j <= MAXNUM:
                if check[j] == 0:
                    check[j] = 1
                
                j += i

# 소수 찾기 수행
is_Prime()

while True:
    n = int(input())

    if n == 0:
        break

    for a in prime:
        if check[n - a] == 0:
            b = n - a # n = a + b 수식을 변형하면 b = n - a가 될 수 있다.

            print(f"{n} = {a} + {b}")
            break
