'''
(1) score를 내림차순으로 정렬

(2) for문을 통해서 최대 숫자를 초과하는 수를 제거한다. → new배열에 넣음

(3) box는 전체 나오는 box의 개수

(4) box수 만큼 for문을 돌고 슬라이싱을 통해서 [[4,4,4],[4,4,4],[2,2,2],[2,1,1]] 와 같이 나눈다.

(5) 최소 사과점수 * 한 상자에 담긴 사과 개수 를 통해서 answer 도출
'''



def solution(k, m, score):
    
    score.sort(reverse=True)
    answer = 0
    new = []
    for i in score:
        if(i <= k):
            new.append(i)

    box = int(len(new) / m)

    contain = []
    idx= 0
    i = 0
    for _ in range(box):
        i += m
        contain.append(new[idx:i])
        idx = i


    for n in contain:
        minN = min(n)
        answer += minN * m
    
    return answer