'''
순위 정보에 따른 팀의 순서를 적절히 정렬이 가능한지 판단한다.
=> 정해진 우선순위에 맞게 전체 팀들의 순서를 나열하는 것 :: 위상정렬을 떠올릴 수 있다.

- 1등팀부터 확인해야한다.
- 위상정렬의 핵심은 진입노드이다
- 시작점은 진입노드가 0개인 노드임

따라서, 1등 -> 2,3,4.. n 등
       2등 -> 3,4 .. n 등

이런 방식으로 노드간 연결해준다.
'''
from collections import deque


def topology_sort(graph , indegree , n):
    global res

    q = deque()

    # 진입노드가 0이면 큐 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    possible = 1 # 가능 여부 :: 큐에 2개 이상 존재하는 상황이 생기면 여러 경로가 발생하므로 고유한 순위 알 수 없음
    cycle = 0 # 사이클 여부 :: 큐에 아무런 값이 없다는 것은 사이클 발생 , 사이클이 발생하면 데이터의 일관성이 없음

    for i in range(n):
        if len(q) == 0:
            cycle = 1
            break

        if len(q) >= 2:
            possible = 0
            break

        now = q.popleft()
        res.append(now)

        for j in range(1,n+1):
            if graph[now][j] == 1: # now -> j 방향이 존재
                indegree[j] -= 1 # now가 꺼내지니 j로 가는 진입노드 제거

                # 진입노드가 0개이면 큐에 넣을 수 있다.
                if indegree[j] == 0:
                    q.append(j)

    return possible , cycle


T = int(input())

for _ in range(T):
    n = int(input())
    rank = list(map(int,input().split())) # 작년 순위

    # 그래프 , 진입노드 생성
    graph = [[0] * (n+1) for _ in range(n+1)]
    indegree = [0] * (n+1)

    for i in range(n):
        for j in range(i+1 , n):
            graph[rank[i]][rank[j]] = 1 # rank[i] -> rank[j] 방향으로 노드를 이음
            indegree[rank[j]] += 1 # 그렇기 때문에  rank[j]의 진입노드가 증가
    
    # 상대적 순위 변화 적용
    m = int(input())
    for _ in range(m):
        a , b = map(int,input().split())

        if graph[a][b] == 1: # a->b 방향의 순위가 있다면 방향 변경
            graph[a][b] = 0 # a -> b 연결 끊음
            graph[b][a] = 1 # b -> a 연결
            indegree[b] -= 1 # b의 진입노드는 감소
            indegree[a] += 1 # a의 진입노드가 증가
        else: # b->a 방향인 상황 ,, 위 상황의 반대임
            graph[b][a] = 0
            graph[a][b] = 1
            indegree[a] -= 1
            indegree[b] += 1

    # 위상 정렬
    res = [] # 결과
    possible , cycle = topology_sort(graph , indegree, n)

    if possible == 0:
        print("?")
    elif cycle == 1:
        print("IMPOSSIBLE")
    else:
        print(*res)