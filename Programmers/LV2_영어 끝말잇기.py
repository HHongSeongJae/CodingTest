def solution(n, words):
    answer = []
    cnt = 1  # n회전 
    people = 1 # 사람 확인
    
    for idx, i in enumerate(words):
        if(idx==0):
            temp = i
            people += 1
            continue
            
        if(people > n):
            people = people % n
            cnt += 1
            
        #앞에 나온단어 확인 / 끝말잇기 규칙 확인
        if((i in words[:idx]) or (i[0] != temp[-1])):
            answer.append(people)
            answer.append(cnt)
            return answer
        else:
            people += 1
            temp = i
            
    answer.append(0)
    answer.append(0)

    return answer