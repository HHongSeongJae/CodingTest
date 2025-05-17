def solution(n):
    answer = []
    tmp = [[0] * n for _ in range(n)]
    
    x,y = -1,0
    num = 1
    
    for i in range(n): # down,up,right
        for j in range(i,n): # 동일 연산 반복 횟수
            if i % 3 == 0: # down
                x += 1
            
            if i % 3 == 1: # right
                y += 1
            
            if i % 3 == 2: # up
                x -= 1
                y -= 1
            
            tmp[x][y] = num
            num += 1
            
    for t in tmp:
        for i in t:
            if i != 0: # [1, 0, 0, 0] 이렇게 배열이 형성되었을 때 0을 제외한 값만 추출
                answer.append(i)
    
    return answer