## 프로그래머스 - 숫자 문자열과 영단어 (99클럽 비기너 문제) level 1

def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    ## 위에 정의한 단어배열만큼 반복
    for i in range(len(words)):
        # 해당 단어가 s 문자열에 있다면? 그 단어를 숫자로 바꿔주기
        if words[i] in s:
            s = s.replace(words[i], str(i)) ## replace의 두번째 변수는 숫자가 아닌 str이어야 한다.

    return int(s) # s로 출력하니까 오류. int(s)로 숫자형식으로 출력하셔요

## 문제 풀이
# replace함수는
# str.replace(문자열, 문자열) 이렇게 사용!