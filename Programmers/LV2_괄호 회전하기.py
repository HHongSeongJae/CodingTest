def solution(s):
    answer = 0
    
    for i in range(len(s)):
        if check(s): 
            answer +=1
        s = s[1:] + s[:1]
    
    return answer
        
def check(a):
    stack = []
    for i in a:
        if(len(stack) == 0): stack.append(i)
        else:
            if( i == ")" and stack[-1] == "("): stack.pop()
            elif( i == "]" and stack[-1] == "["): stack.pop()
            elif( i == "}" and stack[-1] == "{"): stack.pop()
            else: stack.append(i)
    if (len(stack) == 0):
        return 1
    else:
        return 0