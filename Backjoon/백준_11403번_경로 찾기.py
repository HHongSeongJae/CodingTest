'''
(i,i) = 0
0번째 줄의 1번째 숫자 : 1 => 0->1로의 간선 존재
'''
'''
플루이드 워셜
: Dab = min(Dab, Dak + Dkb)
'''

'''
모든 경로에 대한 map을 생성 => 플로이드 워셜 알고리즘 사용
'''

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
                 

# 플루위드 워셜 알고리즘
for k in range(0,n):
    for i in range(0,n):
        for j in range(0,n):
            # i-> k  , k->j 경로가 모두 존재하면 경로가 있는 것
            # 간선에 대한 가중치가 없기 때문에 min으로 최소값을 찾을 필요는 없고, 돌아가는 경로가 가능하면 해당 경로는 1로 설정한다.
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for i in graph:
    print(*i)