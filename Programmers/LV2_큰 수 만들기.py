def solution(number, k):
    answer = []
    
    for n in number:
		    # k가 0이하가 되면 number에서 k개를 제거 완료한 것임으로 나머지는 그대로 넣어주면 된다.
		    # answer 스택이 비어있다면 그냥 넣는다 (비교할 것이 없음)
		    # answer의 가장 마지막 요소와 현재 n의 값 비교
			    # 비교 후, 현재 값이 더 크다면 pop 수행
			    # 이후에도 k > 0 and answer and answer[-1] < n: 이 조건에 맞다면 반복 수행
        while k > 0 and answer and answer[-1] < n:
            answer.pop()
            k -= 1 # 요소를 하나 빼면, number에서 숫자를 제거한 것과 같음
        answer.append(n) # 더 높은 값이 앞 자리에 위치하게 된다
    
    # [:len(number) - k] 처리를 해야하는 이유는
    # 큰 숫자가 앞쪽에 몰려있다면 뒤에 원소가 남아있음에도 불구하고 k개 제거했다면, 뒤에 남은 수가 모두 answer에 append된다.
    # 그래서 len(number)-k 길이의 숫자만 원하므로, answer의 처음부터 len(number)-k 까지만 슬라이싱해줘야 한다.
    return "".join(answer[:len(number) - k])