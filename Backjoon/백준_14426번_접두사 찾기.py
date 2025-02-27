# 트라이 자료구조를 이용한 풀이 방법

# 노드 구현
class Node(object):
    def __init__(self , key , data=None):
        self.key = key
        self.data = data
        self.children = {}

# 트라이 구현
class Trie:
    # 최초 생성시 헤드 노드 생성
    def __init__(self):
        self.head = Node(None) # 데이터 x
    
    # 트라이에 문자열 삽입
    def insert(self, string):
        cur_node = self.head

        for char in string:
            # 현재 노드에 해당하는 글자의 자식이 없다면 추가
            if char not in cur_node.children:
                cur_node.children[char] = Node(char)
            
            # 다음 노드 이동
            cur_node = cur_node.children[char]
        
        # 모든 문자열이 들어가고 마지막 부분에는 data를 넣어주어 마지막임을 표시
        cur_node.data = string
    
    # 트라이에 문자열 조회
    def search(self, string):
        cur_node = self.head

        for char in string:
            # 찾아야 하는 글자가 없다면 단어가 트라이에 존재 x
            if char not in cur_node.children:
                return False
            
            # 해당 단어가 존재하면 다음 노드로 이동하여 확인
            cur_node = cur_node.children[char]
        
        # 반복이 끝났다면 해당 단어(string)은 존재
        return True

#######
n , m = map(int,input().split())

T = Trie()

for _ in range(n):
    T.insert(input())

res = 0
for _ in range(m):
    if T.search(input()):
        res += 1
print(res)