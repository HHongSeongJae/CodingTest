def solution(elements):
    result = set()
    
    elen = len(elements)
    elements = elements * 2
    
    for i in range(elen):
        for j in range(elen):
            result.add(sum(elements[j:j+i+1]))
    return len(result)