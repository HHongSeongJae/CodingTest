def solution(n):
    answer = n

    #1개수 찾기
    binary = bin(n)
    num = binary.count('1')
    
    #다음 큰 수 찾기
    while(True):
        answer = answer + 1
        binary_count = bin(answer).count('1')
        if(binary_count == num): break
    
    return answer