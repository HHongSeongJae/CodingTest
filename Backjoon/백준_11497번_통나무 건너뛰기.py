'''
통나무를 원형으로 구성
인접한 통나무 높이차가 가장 큰 값이 해당 배열의 난이도
난이도가 최소가 되도록 구성
'''

'''
1 . 리스트 정렬
2 . 정렬된 리스트의 순서대로 새로운 리스트의 양끝에 배치
    2-1. 예를들어 정렬시킨 리스트가 2 4 5 7 9 라고하면
         2번으로 배치하게 되면 2 5 9 7 4가 된다.
         
'''

# T = int(input())

# for _ in range(T):
#     N = int(input())
#     L = list(map(int,input().split()))

#     #정렬
#     L.sort()

#     level = 0
#     for i in range(2,N):
#         level = max(level, abs(L[i] - L[i-2]))

#     print(level)

T = int(input())

for _ in range(T):
    N = int(input())
    L = list(map(int,input().split()))

    #정렬
    L.sort()

    #배치
    new_list = L[::2]
    new_list2 = L[1::2][::-1]

    new = new_list + new_list2

    # 인접 크기 계산
    result = new[0] - new[-1]
    for i in range(1,N):
        result = max(result , abs(new[i] - new[i-1]))
    
    print(result)