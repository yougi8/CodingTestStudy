## 프로그래머스 Lv3 표 편집 - https://school.programmers.co.kr/learn/courses/30/lessons/81303
import heapq

def solution(n, k, cmd):
    answer = ''

    # down의 첫번째 값이 현재 선택된 값
    up, down = [], []
    for i in range(n):
        if i < k:
            heapq.heappush(up, -i)
        else:
            heapq.heappush(down, i)

    deleted = []
    for c in cmd:
        # 삭제
        if c[0] == 'C':
            deleted.append(heapq.heappop(down))

            # 방금 삭제한 값이 마지막 행이었으면 up 배열에서 하나 넘겨주기
            if len(down) == 0:
                heapq.heappush(down, -heapq.heappop(up))

        # 복구
        elif c[0] == 'Z':
            back = deleted.pop()
            # 복구된 값이 현위치보다 작으면 up에 넣어주기
            if back < down[0]:
                heapq.heappush(up, -back)
            else:
                heapq.heappush(down, back)

        # 이동
        elif c[0] == 'D':
            number = int(c[2:])
            for i in range(number):
                heapq.heappush(up, -heapq.heappop(down))

        elif c[0] == 'U':
            number = int(c[2:])
            for i in range(number):
                heapq.heappush(down, -heapq.heappop(up))

    arr = []
    for i in range(len(up)):
        up[i] *= -1
    arr.extend(up)
    arr.extend(down)

    arr = set(arr)
    for i in range(n):
        if i in arr:
            answer += 'O'
        else:
            answer += 'X'

    return answer

## 문제 풀이
# 리스트에서 검색하는 것은 시간이 많이 걸린다!
# 그래서 마지막에 arr를 set()으로 형 변환 시켜서 검색 시간을 n으로 줄여야지 효율성 통과가 됨 (중요!!)