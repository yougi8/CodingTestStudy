## 프로그래머스 - 주식가격 Lv2 https://school.programmers.co.kr/learn/courses/30/lessons/42584
def solution(prices):
    n = len(prices)

    # answer 초기화 : 끝까지 가격이 안 떨어진 값으로 저장한다
    answer = []
    for i in range(n):
        answer.append(n - i - 1)

    ## dp로 얻은 값 저장(살펴본 prices의 인덱스 번호를 저장한다)
    arr = []

    for i, price in enumerate(prices):
        ## 앞에 나온 price 가격이 (arr에 인덱스로 저장되어있음) 현재 보는 가격보다 높을 때 -> 가격 떨어진 것임
        while arr and prices[arr[-1]] > price:
            ## 앞에 나온 price 기준으로 가격이 떨어진거니까 해당 index를 가져와서 값을 업데이트
            ## i는 더 낮은 가격이 등장한 시점, idx는 떨어짐 당한 아이니까 그 둘의 차가 버틴 시간이 된다
            idx = arr.pop()
            answer[idx] = i - idx

        # 인덱스 저장해줌
        arr.append(i)

    return answer

## 이제 이런 문제는 절대 for문 돌아서는 해결이 안 된다는 것을 알았다.
## 그렇다면 dp를 써야 하는데..
## 주로 스택을 활용한다!