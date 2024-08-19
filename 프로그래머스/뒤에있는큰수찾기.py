## 프로그래머스 - 뒤에 있는 큰 수 찾기 https://school.programmers.co.kr/learn/courses/30/lessons/154539

def solution(numbers):
    N = len(numbers)
    answer = [-1] * N
    arr = []

    for idx, num in enumerate(numbers):
        while arr and numbers[arr[-1]] < num:
            answer[arr.pop()] = num
        arr.append(idx)

    return answer
solution([2,3,3,5])
solution([9, 1, 5, 3, 6, 2])