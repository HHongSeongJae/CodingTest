'''
칠해야 하는 타일인 section 배열에 있는 수를 기준으로 칠하는 타일의 시작점이 된다.
따라서 start = section[0] 이고 이전 반복에서 section이 칠해졌다면 start는 다음 section으로 넘어간다 ( start = section[i] ) 
'''


def solution(n, m, section):
    answer = 1
    start = section[0]
    
    for i in range(1, len(section)):
        if (section[i] - start >= m):
            answer += 1
            start = section[i]
        
    return answer