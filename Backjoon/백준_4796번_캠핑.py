import sys

input = sys.stdin.readline
count = 0
while True:
    l,p,v = map(int,input().split())

    if l == 0 and p == 0 and v == 0:
        break
    
    count += 1

    # 휴가 기간에서 연속적으로 캠핑장에 있을 수 있는 날을 구하고 그 기간동안 사용 가능한 날을 곱해준다.
    use = (v // p) * l

    # 완전히 나누어 떨어지지 않았다면 남는 휴가 기간에 대해서 고려
    if (v % p) != 0:
        temp = (v%p) # 남은 기간

        # 남은 기간이 연속 캠핑장 사용기간 보다는 작고, 그 기간동안 사용할 수 있는 날 보다 크면 사용할 수 있는 날 만큼 캠핑장 이용가능
        if l <= temp <= p:
            use += l
        # 위 조건이 아니라면 남은 날에만 이용가능
        else:
            use += temp

    print(f"Case {count}: {use}")