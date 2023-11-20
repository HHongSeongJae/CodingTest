from collections import deque

def bfs(x,y, maps, queue):
    
    #상하 좌우를 확인하기 위한 배열
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    queue.append((x,y)) #현재 위치를 큐에 넣는다.
    
    while queue:  #큐가 empty상태까지 계속 반복한다.
        x,y = queue.popleft() #선입선출이기 때문에 큐의 좌측부터 값을 뺀다.
        
        #현재 위치로 부터 상하좌우 확인
        for i in range(4): 
            nx = x + dx[i]
            ny = y + dy[i]
            
            #maps범위를 벗어나는 경우 제외
            if (nx < 0 or nx >= len(maps) or ny<0 or ny>=len(maps[0])): continue
            #지나갈 수 없는 경우 제외
            if (maps[nx][ny] == 0): continue
            #지나 갈 수 있는 길을 발견
            if (maps[nx][ny] == 1):
                maps[nx][ny] = maps[x][y] + 1  #찾은 위치(nx,ny)를 현재 위치의 값 +1을 통해서 거리를 유지한다. 
                queue.append((nx,ny)) #(nx,ny)가 현재위치가 되도록 큐에 넣어준다. => 반복
    return maps[len(maps)-1][len(maps[0])-1] #maps의 가장 우측 하단 좌표값이 최단 거리가 된다.

def solution(maps):
    queue = deque()
    answer = bfs(0,0, maps, queue)
    return -1 if answer == 1 else answer 
#bfs결과 1의 값이 나왔다는 것은 block으로 인해서 도착할 수 있는 경로가 존재하지 않음을 의미