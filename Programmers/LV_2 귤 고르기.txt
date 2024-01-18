def solution(k, tangerine):
    answer = 0
    
    temp = {}
    
    #dict형태로 tangerine 값을 넣어준다.
    for i in tangerine:
        if i in temp:
            temp[i] += 1 #이전에 존재
        else:
            temp[i] = 1  #새로운 크기
            
    #내림차순 정렬 value기준
    temp2 = dict(sorted(temp.items(), key=lambda x : x[1], reverse=True))
    
    #개수가 가장 많은 크기부터 담는다.
    for j in temp2:
        if k <= 0 :
            return answer
        k -= temp2[j]
        answer += 1
    
    return answer