def solution(progresses, speeds):
    answer = []
    queue = []
    
    for i, j in zip(progresses , speeds):
        if( (100-i) % j == 0 ):
            days = (100-i) // j
        else:
            days = (100-i) // j + 1
        queue.append(days)
        
    index = 0
    temp = 0
    for z in range(len(queue)):
        if(queue[index] < queue[z]): # 현재 process 소요 시간보다 더 큰 소요시간 등장
            answer.append(z - index)   
            index = z
            
    #남은 값 처리
    answer.append(len(queue)-index)
            
    return answer