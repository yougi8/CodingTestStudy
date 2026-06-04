## 프로그래머스 Lv.2 점프와 순간이동 - https://school.programmers.co.kr/learn/courses/30/lessons/12980
def solution(n):
    ans = 0
    
    ## n부터 0이 될때까지 역순으로 계산하기
    while n>0 : 
        
        ## 2배로 순간이동 했을 경우 -> 카운팅 하지 않음. n을 2로 나눔
        if n%2 == 0:
            n //= 2
        
        ## +1로 갔을 경우 -> 카운팅함. n에서 1 뺀 값으로 업데이트 함
        else:
            n -= 1
            ans += 1
            
    return ans

## 그리디 : 매순간 최선의 선택을 함!!!