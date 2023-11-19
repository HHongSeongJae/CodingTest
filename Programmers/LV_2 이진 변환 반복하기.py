def solution(s):
    answer = []
    
    zeroDelete = 0
    count = 0
    
    while(True):
        if(s == "1"): 
            break
        
        slen = len(s)
        s = s.count('0')
        
        zeroDelete = zeroDelete + s
        count = count + 1
        s = bin(slen - s)[2:]     # 0제거 후 길이 -> 이진수로 변경

    answer.append(count)
    answer.append(zeroDelete)
        
    return answer