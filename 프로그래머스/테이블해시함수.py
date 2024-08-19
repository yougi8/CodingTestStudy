## 프로그래머스 - 테이블 해시 함수 https://school.programmers.co.kr/learn/courses/30/lessons/147354
def solution(data, col, row_begin, row_end):
    answer = 0

    data.sort(key=lambda x: (x[col - 1], -x[0]))
    for i in range(row_begin - 1, row_end):
        total = 0
        for num in data[i]:
            total += num % (i + 1)

        ## XOR 연산 : ^
        answer ^= total
    return answer