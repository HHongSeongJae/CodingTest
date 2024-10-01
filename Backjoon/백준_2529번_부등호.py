'''
- 0~9로 생성할 수 있는 숫자 중 최대값/최솟값 출력
'''
# 숫자를 선택하는 함수 -> 재귀적으로 구현할 것임
def check(x,y,op):
    #아니면 유효한지 확인
    if op == '>':
        if x < y:
            return 0
    
    if op == '<':
        if x > y:
            return 0
    
    return 1

def select(idx , num):
    if idx == k+1:
        answer.append(num)
        return

    for i in range(10):
        if visited[i] == 1: # 이미 사용한 숫자
            continue
        
        if idx == 0 or check(num[idx-1],str(i),key[idx-1]): # 백트래킹 조건 : check를 통해서 유효하지 못한 부등호가 된다면 select 함수 호출 x
            visited[i] = 1 # 방문처리
            select(idx+1, num + str(i)) # 1+2 = 12와 같이 수를 이어붙여야하기 때문에 str형태로 변환 후 더해준다.
            visited[i] = 0 # visited[i]에 대한 모든 처리가 끝났으니 다시 돌려준다.

k = int(input())
key = input().split() # 부등호
visited = [0] * 10 # 0~9 숫자 사용 여부
answer = [] # 정답
select(0 , '') # num은 str 타입으로 넣어줘야 한다.
answer.sort()

print(answer[-1])
print(answer[0])