def solution(s):
    new_s = list(map(int, s.split(' ')))  #문자열을 list형태로 변환
    new_s.sort()
    return str(new_s[0]) + ' ' + str(new_s[-1]) #list형태를 문자열로 만들기