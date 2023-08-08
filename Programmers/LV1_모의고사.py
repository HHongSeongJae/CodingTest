# % (modulation) 연산자 활용 (원형 큐와 같은 원리 활용)

def solution(answers):   
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    count1, count2, count3 = 0 , 0 , 0
    
    for i in range(len(answers)):
        idx1 = i % len(one)
        idx2 = i % len(two)
        idx3 = i % len(three)
        
        if(answers[i] == one[idx1]): 
            count1 += 1 
        if(answers[i] == two[idx2]): 
            count2 += 1 
        if(answers[i] == three[idx3]): 
            count3 += 1 
        
    k = max(count1, count2, count3)
    
    if(count1 == k):
        answer.append(1)
    if(count2 == k):
        answer.append(2)
    if(count3 == k):
        answer.append(3)
    
    return answer