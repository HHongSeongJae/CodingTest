'''

3 2
1 4
4 1
2 3
5 5

# x축 기준 정렬
1 4
2 3
3 2
4 1
5 5
'''

''' 
<초기> 1차,2차 각각 정렬을 해서 순위의 가중치를 만들어서 더해주는 방식을 하려고 함
<초기> 하지만 이는 문제를 잘못이해한 것이었다.
<초기> 그래서 알고리즘을 참조하니 그리디 방식의 알고리즘을 파악

알고리즘 참조
1. 1차 성적을 기준으로 정렬한다.
2. 정렬의 결과로 1차성적 1등을 기준 값으로 설정
    2-1. 1차성적 1등의 2차성적값과 1차성적 2등의 2차성적값을 비교했을 때 1차성적 2등의 2차성적값이 더 높다(값이 작다)면 합격자 +1 , 아니면 지금까지 합격자수를 출력하며 종료
    2-2. 위 과정을 반복
'''

### 첫 풀이 ==> 4852 ms
# import sys

# T = int(input())

# for _ in range(T):
#     N = int(input())

#     score = []

#     for i in range(N):
#         score.append(list(map(int,sys.stdin.readline().split())))

#     #1차 성적 기준 정렬
#     new_score = sorted(score, key=lambda x : x[0])

#     result = 1 #1등은 반드시 합격이라 1로 시작
#     temp = score[0][1]
#     for i in range(1,N):
#         if temp >= score[i][1]:
#             result += 1
#             temp = score[i][1]    
    
#     print(result)


'''
T : 2 동작 과정
[[1, 4], [2, 5], [3, 6], [4, 2], [5, 7], [6, 1], [7, 3]]

1 : [1,4] 와 [2,5] 비교 1<2 , 4<5  ,, 불합  => 1
2 : [1,4] 와 [3,6] 비교 1<3 , 4<6  ,, 불합
3 : [1,4] 와 [4,2] 비교 1<4 , 4>2  ,, 합격 ,, 기준 [4,2] 로 변경  => 2
4 : [4,2] 와 [5,7] 비교 4<5 , 2<7  ,, 불합
5 : [4,2] 와 [6,1] 비교 4<6 , 2>1  ,, 합격 ,, 기준 [6,1] 로 변경  => 3
6 : [6,1] 와 [7,3] 비교 6<7 , 1<3  ,, 불합
'''

### 정렬시 key=lambda를 통해서 기준을 정해주면 더 빠른 시간 수행이 이뤄짐
### 새로운 리스트를 생성하는 sorted보다 기존 리스트에 정렬을 수행하는 sort가 더 빠름
### 가장 짧은 수행시간  => 3824ms
import sys

T = int(input())

for _ in range(T):
    N = int(input())

    score = []

    for i in range(N):
        score.append(list(map(int,sys.stdin.readline().split())))

    #1차 성적 기준 정렬
    score.sort(key=lambda x : x[0])

    result = 1 #1등은 반드시 합격이라 1로 시작
    temp = score[0][1]
    for i in range(1,N):
        if temp >= score[i][1]:
            result += 1
            temp = score[i][1]    
    
    print(result)
