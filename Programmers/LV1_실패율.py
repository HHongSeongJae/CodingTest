def solution(N, stages):
    temp = {}
    n = len(stages) 

    for i in range(1,N+1): # 1~N번만 반복
        if(n != 0):
            count = stages.count(i)  #.count(i) => i값과 일치하는 개수를 return
            temp[i] = count / n #오차율
            n -= count  #첫번째 스테이지, 두 번째 스테이지... 구현을 위함
        else:   #이 조건을 주지 않으면 divison by zero 런타임 오류 발생
            temp[i] = 0
    
    return sorted(temp, key = lambda i : temp[i], reverse=True)