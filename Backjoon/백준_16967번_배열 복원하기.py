h , w  , x , y = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(h+x)]

for i in range(h):
    for j in range(w):
        if 0 <= i + x < h+x and 0 <= j + y < w + y:
            graph[i+x][j+y] = graph[i+x][j+y] - graph[i][j]

# for i in range(h):
#     for j in range(w):
#         print(graph[i][j] , end=' ')
#     print()

for i in range(h):
    print(' '.join(map(str,graph[i][:w])))