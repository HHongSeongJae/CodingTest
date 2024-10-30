#  두 팀의 인원수는 같지 않아도 되지만, 한 명 이상이어야 한다. 라는 조건이 추가되었다.

n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]

def go(idx , start , link):
    if idx == n:
        # 팀원의 수는 같을 필요는 없지만 한 명 이상 있어야 하므로 0명인 팀이 존재하면 불가능한 상황 : 종료
        if len(start) == 0 or len(link) == 0:
            return - 1
        
        t1 = 0 # start
        t2 = 0 # link

        # start와 link팀에는 각각 사람의 index 번호가 들어가있다.
        # 또한 start와 link의 팀원들의 숫자가 정해져있지 않기 때문에 range(n//2)와 같은 것은 불가능하다.
        # 그래서 start와 link에 있는 사람번호를 각각 꺼내서 능력치를 추가한다.
        for si in start:
            for sj in start:
                if si == sj:
                    continue

                t1 += s[si][sj]
        
        for li in link:
            for lj in link:
                if li == lj:
                    continue

                t2 += s[li][lj]
        
        diff = abs(t1-t2)
        return diff
    
    # 팀 선택
    ans = -1
    #start 팀
    t1 = go(idx+1 , start + [idx] , link)
    if ans == -1 or (t1 != -1 and ans > t1):
        ans = t1
    #link 팀
    t2 = go(idx+1 , start , link+[idx])
    if ans == -1 or (t2 != -1 and ans > t2):
        ans = t2
    
    return ans

print(go(0,[],[]))