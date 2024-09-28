T = int(input())

for _ in range(T):
    M,N,x,y = map(int,input().split())

    # xp = i * M + x

    # % 연산을 위해서 1 <= x <= M 을 0 <= x < M 으로 해준다.
    x -= 1
    y -= 1

    # x에서 시작
    year = x
    i = 1
    while year < N*M:
        # y를 찾게 되면 끝난다.
        if year % N == y:
            print(year + 1)
            break

        # year = i % M = 3 의 검산식 => year = i * M + x
        year = i * M + x
        i += 1

    else:
        print(-1)