def solution(s):
    answer = ''
    
    s = s.split(' ')
    
    a=[]
    for i in s:
        a.append(i.capitalize())

    answer = ' '.join(a) 
        
    return answer