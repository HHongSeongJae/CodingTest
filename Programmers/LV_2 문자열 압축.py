## 첫 풀이
def solution(s):
    answer = 0
    
    l = len(s)
    ans = []
    for i in range(1 , l+1): # 문자를 쪼개는 단위
        res = '' # 쪼갠 문자열 관리
        cnt = 1 # 몇 번 연속되는 규칙인지 확인
        tmp = s[:i] # 첫 규칙
        
        j = i
        while j <= (l + i - 1): # l+i-1 까지로 범위를 지정해야 문자를 쪼개는 단위가 딱 떨어지지 않더라도 나머지 문자에 대한 처리를 할 수 있다.
            tmp2 = s[j:j+i] # 다음 규칙 생성
            
            # 이전 규칙과 동일한지 확인
            if tmp == tmp2: # 같다면 cnt 증가
                cnt += 1
            else: # 다르다면 새로운 규칙이 등장한 것
                if cnt == 1: # 새로운 규칙이 등장했지만 이전 규칙이 한번밖에 안나온 경우
                    res += tmp
                    tmp = tmp2
                    cnt = 1
                else: # 이전 규칙이 여러 번 나왔던 경우
                    res += (str(cnt) + tmp)
                    tmp = tmp2
                    cnt = 1
                        
            j += i
    
        # i번씩 쪼갠 결과
        ans.append(len(res))
    answer = min(ans)
    return answer

# 두번째 풀이
def solution(s):
    answer = 0
    ans = []
    l = len(s)
    
    for i in range(1, l+1): # 쪼개는 단위
        res = ''
        cnt = 1
        tmp = s[:i]
        
        for j in range(i , l + i , i): # l+i 까지로 범위를 지정해야 문자를 쪼개는 단위가 딱 떨어지지 않더라도 나머지 문자에 대한 처리를 할 수 있다.
            tmp2 = s[j : j+i] # 다음 규칙 생성
            
            # 이전 규칙과 동일한지 확인
            if tmp == tmp2: # 같다면 cnt 증가
                cnt += 1
            else: # 다르다면 새로운 규칙이 등장한 것
                if cnt != 1: # 이전 규칙이 여러 번 나왔던 경우
                    res += (str(cnt)+tmp)
                    tmp = tmp2
                    cnt = 1
                else: # 새로운 규칙이 등장했지만 이전 규칙이 한번밖에 안나온 경우
                    res += tmp
                    tmp = tmp2
                    cnt = 1
        ans.append(len(res))
    
    answer = min(ans) 
    return answer




