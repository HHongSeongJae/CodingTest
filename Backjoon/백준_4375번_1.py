while True:
    # 테스트 케이스의 개수가 정해지지 않은 문제이기 때문에 Try except문을 사용한다.
    try:
        n = int(input())
    except:
        break

    num = 0 # 1로만 이뤄진 n의 배수
    i = 1 # 자릿수

    # 나누어 떨어지는 경우까지 구현
    while True:
        num = (num * 10) + 1 # 이전수를 이용해서 다음수를 만들어주는 방법
        num %= n

        if num == 0: 
            print(i)
            break
        
        i += 1