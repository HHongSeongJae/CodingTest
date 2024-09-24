N = int(input())
M = int(input())

if M != 0:
    broken = list(map(int,input().split()))
else: # 고장난 번호가 없는 경우
    broken = []

# 버튼으로 이동할 수 있는지 확인 (브루트 포스)
def check(c): # num 은 0 <= C <= 1,000,000 사이의 숫자이다.
    # c가 0인 경우
    if c == 0:
        if c in broken: # 이 고장난 경우
            return 0 # 번호로 이동할 방법이 없다
        else:
            return 1 # 0한번만 누르면 바로 이동 가능
        
    # 나머지 경우
    # c의 자릿수마다 확인한다.
    len = 0
    while c > 0:
        # 해당 c의 자릿수중 고장난 번호가 존재한다면 최소의 방법이 될 수 없다.
        if (c % 10) in broken:
            return 0
        
        len += 1
        c //= 10
    
    return len

# 버튼으로 최대한 이동 후 +/- 으로 이동할 수 있는 횟수를 구한다.
res = abs(N - 100) # 기준 숫자가 100 .. 만약 N이 100이면 누르는 횟수는 0회가 될 수 있다.

for c in range(1000001): # 0 <= C <= 1,000,000
    len = check(c)

    # len이 0이라는 것은 번호를 눌러서 이동할 수 없는 경우
    if len > 0:
        count = abs(c-N)

        if res > len + count:
            res = len + count

print(res)