def solution(people, limit):
    answer = 0
    people.sort()
    
    first = 0
    last = len(people) - 1
    
    while first<last:
        if(people[first] + people[last] <= limit):
            first+=1
            answer+=1
        last-=1
        
    return len(people) - answer

'''
- first와 last의 포이터를 활용하여 전체 경우를 탐색한다 [그리디 알고리즘]
- 일단 first 와 last 포인터가 겹치기 전까지 limit 조건 이내의 무게가 가능한 경우의 case를 탐색한다.
- **그럼 answer에는 한번에 보트를 태울 수 있는 경우의 수가 생성된다. 그럼 나머지는 한명씩 보트에 태워서 보내게 될 것임**
- 따라서 reutrn len(people) - answer을 해주게 되면 전체의 경우의 수가 계산이 된다.
'''