n = int(input())
graph = [list(input().split()) for _ in range(n)]

# DFS를 활용하여 장애물 설치 (조합 구현)
def defense(cnt):
    if cnt == 3:
        # 순회하면서 선생님을 찾는다.
        for ti in range(n):
            for tj in range(n):
                if graph[ti][tj] == 'T':
                    # 전체 그래프를 순회하며 선생님(T)를 찾은 후 해당 위치에서 4가지 방향으로 graph의 끝까지 확인하며 가능여부 확인
                    for d in range(4):
                        # 선생님이 감시하는 함수 (파라미터 : 현재의 방향)
                        # 리턴 : 0 (학생이 발견된 경우) => ok = False 변경 및 반복문 종료 후 다른 장애물(O)의 조합을 구한다.
                        #       1 (장애물을 만난 경우 / 학생을 발견하지 못한 경우) => 다음 방향 수행
                        tmp = watch(graph , ti , tj, d)

                        if tmp == 0:
                            return # return을 통해 다음 장애물 조합을 구한다.

        # 모든 순회를 마쳤는데 ok == True이면 가능한 경우 이므로 yes를 출력하고 프로그램을 종료시킨다.
        print("YES")
        exit()
    
    for xx in range(n):
        for yy in range(n):
            if graph[xx][yy] == 'X':
                graph[xx][yy] = 'O'
                defense(cnt + 1)
                graph[xx][yy] = 'X'

# 선생님이 감시하는 함수
def watch(graph , nowx , nowy, direct): # 방향 번호 : 상(0) , 하(1) , 좌(2) , 우(3)
    if direct == 0: # 상 방향
        while True:
            nowx -= 1
            
            if nowx < 0:
                break

            if graph[nowx][nowy] == 'O': # 장애물 만났다면 => 1리턴
                return 1
            elif graph[nowx][nowy] == 'S': # 학생을 만났다면 => 0리턴
                return 0
        
        # 학생 / 장애물을 만나지 않은 경우
        return 1
    elif direct == 1: # 하 방향
        while True:
            nowx += 1
            
            if nowx >= n:
                break

            if graph[nowx][nowy] == 'O': # 장애물 만났다면 => 1리턴
                return 1
            elif graph[nowx][nowy] == 'S': # 학생을 만났다면 => 0리턴
                return 0
        
        # 학생 / 장애물을 만나지 않은 경우
        return 1
    elif direct == 2: # 좌 방향
        while True:
            nowy -= 1
            
            if nowy < 0:
                break

            if graph[nowx][nowy] == 'O': # 장애물 만났다면 => 1리턴
                return 1
            elif graph[nowx][nowy] == 'S': # 학생을 만났다면 => 0리턴
                return 0
        
        # 학생 / 장애물을 만나지 않은 경우
        return 1
    elif direct == 3: # 우 방향
        while True:
            nowy += 1
            
            if nowy >= n:
                break

            if graph[nowx][nowy] == 'O': # 장애물 만났다면 => 1리턴
                return 1
            elif graph[nowx][nowy] == 'S': # 학생을 만났다면 => 0리턴
                return 0
        
        # 학생 / 장애물을 만나지 않은 경우
        return 1
    
defense(0)

# defense에서 종료되지 않고 나온다면 불가능한 경우
print("NO")