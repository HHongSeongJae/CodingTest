# 루트 노드를 찾아간다.
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합친다.
def union_parent(parent, number, a, b):
    a = find_parent(parent , a)
    b = find_parent(parent , b)

    # 해당 문제에서는 노드의 key 값이 문자열이다.
    # 그래서, 크기 비교가 아니라 같다 / 다르다로 비교할 수 있다.
    if a != b:
        parent[b] = a
        number[a] += number[b] # 현재 집합에 포함된 원소들의 개수를 number에 유지한다.
    
    print(number[a])

t = int(input())

for _ in range(t):
    f = int(input())

    parent = {}
    number = {}

    for i in range(f):
        a , b = input().split()

        if a not in parent:
            parent[a] = a
            number[a] = 1

        if b not in parent:
            parent[b] = b
            number[b] = 1
        
        union_parent(parent, number, a, b)