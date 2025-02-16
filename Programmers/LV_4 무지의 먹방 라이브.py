from collections import deque

def solution(food_times, k):
    answer = 0
    
    if sum(food_times) <= k:
        answer = -1
        return answer
    
    q = []
    # [time,idx] 형식으로 q 리스트를 만든다.
    for idx , time in enumerate(food_times):
        q.append([time,idx+1])
    
    # 그리디 알고리즘 사용을 위하여 음식을 먹는데 소요되는 시간이 가장 작은 값 순서대로 정렬한다.
    q.sort(key=lambda x : x[0])
    
    # q 리스트를 큐로 변환 (popleft) 사용을 위함
    # pop(0)을 리스트에서 사용하게 된다면 제거된 부분을 한칸씩 앞당겨야하므로 O(N) 소모
    # 하지만, 큐는 앞,뒤로 요소가 빠질 수 있으므로 O(1)이다.
    q = deque(q)
    
    eat_time = 0 # 현재까지 음식을 먹는데 소모된 시간
    pre_eat_time = 0 # 이전 음식을 먹는데 소모된 시간
    length = len(q) # 전체 음식의 개수
    
    # 현재까지 음식을 먹는데 소모된 시간 + 현재 음식을 먹게되면서 소요된 시간이 k 보다 크면 다음 음식을 찾는 연산을 수행한다.
    while eat_time + (q[0][0] - pre_eat_time) * length <= k:
        tmp = q.popleft()
        eat_time += (tmp[0] - pre_eat_time) * length
        length -= 1 # 음식 하나를 모두 먹었다.
        pre_eat_time = tmp[0]
    
    # 현재 q는 큐이기 때문에 정렬이 불가능하다.
    # 그래서 q2를 만들어서 q를 리스트로 다시 변환하는 과정을 거친다.
    q2 = []
    while True:
		    # q의 요소가 모두 빠졌다면 반복 종료
        if len(q) == 0:
            break
        
        # q2에 q의 요소를 넣는다.
        q2.append(q.popleft())
    
    q2.sort(key=lambda x : x[1]) # 음식의 index번호가 작은 순서대로 정렬
    find_idx = (k - eat_time) % length # 현재 음식을 먹는데 걸린 시간에서 k까지의 남은 시간을 구해서 남은 음식 수 만큼 % 연산하면 다음 음식의 index 값이 나온다.
    answer = q2[find_idx][1]
    return answer