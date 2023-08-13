def solution(lottos, win_nums):
    answer = []
    
    zerocnt = lottos.count(0)
    rank=[6,6,5,4,3,2,1]  #rank배열을 활용해 등수를 나타냄
    cnt=0
    
    for i in win_nums:
        if i in lottos:
            cnt+=1
            
    answer.append(rank[zerocnt+cnt])
    answer.append(rank[cnt])
    
    return answer