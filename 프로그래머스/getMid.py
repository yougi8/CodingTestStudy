## 프로그래머스 - 가운데글자 가져오기 Lv.1 (99 비기너 문제)

def solution(s):
    answer = ''
    length = len(s)
    if length%2==0:
        answer += s[(length//2)-1:(length//2)+1]
    else:
        answer += s[length//2]
    return answer

## 문제 풀이
# - 길이가 짝수면, s[중간값-1:중간값+1] 을 추가하면 되고
# - 길이가 홀수면 s[중간값]이 답이다.