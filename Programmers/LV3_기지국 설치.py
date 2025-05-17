def solution(n, stations, w):
    answer = 0
    wide_w = w * 2 + 1
    
    # 시작 지점은 1
    before = 1
    for s in stations:
        # 만약, s의 커버 범위가 0이전까지라면 s-w < 0 이 된다. -> 자연스럽게 s-w-before 도 <0
        # 이런 상황이면 시작 위치가 1이 아닌 경우이므로, 기지국을 놓을 필요 없이, before의 위치를 s+w+1 위치로 옮기는 것만 수행
        if s - w - before > 0:
            # 1~(s-w) 범위에 기지국을 설치할 수 있는 상황
            # s - w - before 길이 구간에 최대한 기지국을 몇 개 설치할 수 있는지 연산
            answer += (s - w - before) // wide_w
            
            # (s - w - before) // wide_w 가 나누어 떨어지지 않는다면 전체의 범위를 커버할 수 없으므로 기지국 1개 추가 설치
            if (s - w - before) % wide_w != 0:
                answer += 1
        # 다음 기지국 설치를 위해 시작 위치를 s+w+1 위치로 옮긴다.
        before = s + w + 1
    
    # before = s + w + 1 와 같이 기지국의 마지막 커버범위 + 1을 기준으로 수행했다 (제일 처음 before도 1로 시작)
    # (n+1) - before < 0 이라는 것은 "예시1"과 같은 상황 처럼 11 위치의 기지국의 우측 커버 범위는 도시의 크기를 벗어남
    # 그래서 before값이 도시 크기 밖으로 넘어간 상태이고, 더 이상 연산 필요 x
    if (n+1) - before > 0:
        # 해당 상황은 마지막 기지국에서 끝까지의 범위에 새로운 기지국을 설치할 수 있는 상황
        answer += (n + 1 - before) // wide_w
        
        if (n+1-before) % wide_w != 0:
            answer += 1

    return answer