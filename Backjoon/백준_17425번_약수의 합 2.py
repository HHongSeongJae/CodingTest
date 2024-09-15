# PyPy3 사용
MAXNUM = 1000000 # 문제의 최대 자연수

# 반복문을 통해 초기화
# f = [1 for _ in range(MAXNUM+1)]
# g = [0 for _ in range(MAXNUM+1)]

### 곱셈을 통해서 초기화
f = [1] * (MAXNUM+1)
g = [0] * (MAXNUM+1)

# f(a)를 미리 구한다
def Prime():
    for i in range(2, MAXNUM+1):
        for j in range(1, MAXNUM+1):
            if i*j > MAXNUM:
                break

            f[i*j] += i

# 누적합을 이용해서 g(x)를 계산
def sumPrime():
    for i in range(1,MAXNUM+1):
        g[i] = g[i-1] + f[i]

# 테스트 케이스 및 자연수 입력
T = int(input())

Prime()
sumPrime()

answer = []

for i in range(T):
    N = int(input())

    # 입력된 자연수를 미리 만들어둔 리스트에서 찾아서 출력
    # print(g[N])  # 테스트 케이스마다 출력하게 되면 print에 대한 시간이 소요되어서 해당 문제에서는 시간초과 발생
    answer.append(g[N])

print('\n'.join(map(str,answer)) + '\n')