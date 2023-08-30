def solution(citations):
    answer = 0
    citations.sort(reverse=True) #내림차순
    
    for i in range(len(citations)):
        if (citations[i] < i+1):
            return i
    return len(citations) #H-index가 마지막에 존재할 경우임