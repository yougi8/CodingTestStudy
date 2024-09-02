## 프로그래머스 - Lv2. 호텔 대실 https://school.programmers.co.kr/learn/courses/30/lessons/155651
import heapq

def solution(book_time):
    answer = 0

    for i in range(len(book_time)):
        sh = book_time[i][0][0:2]
        sm = book_time[i][0][3:5]
        eh = book_time[i][1][0:2]
        em = book_time[i][1][3:5]

        book_time[i][0] = int(sh) * 60 + int(sm)
        book_time[i][1] = int(eh) * 60 + int(em) + 10

    book_time.sort()
    q = []

    for book in book_time:
        if q and book[0] >= q[0]:
            heapq.heappop(q)
        else:
            answer += 1
        heapq.heappush(q, book[1])
    return answer

## 문제 풀이
# 입실시간, 퇴실시간을 분단위로 우선 바꾸고
# 입실시간을 기준으로 오름차순 정렬
# heapq를 만들고, 퇴실시간만 저장해줄 것임
# book_time을 순서대로 돌면서 확인할건데
# heapq에 값이 있고 (룸을 쓰고있는 상태), 0번째 퇴실시간이 지금 입실시간보다 전이면 그 방을 써도 됨.
# 그러니까 if문에서 heapq에 있는 값을 지워준다 (방 빼!)
# 그렇지 않은 경우에는 다른 방을 써야하니까 answer += 1