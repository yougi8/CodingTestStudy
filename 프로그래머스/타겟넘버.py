## 프로그래머스 - 타겟넘버 (dfs)
def dfs(numbers, target, depth):
    global answer
    if depth == len(numbers):
        if sum(numbers) == target:
            answer += 1
        return

    dfs(numbers, target, depth + 1)
    numbers[depth] *= -1
    dfs(numbers, target, depth + 1)


def solution(numbers, target):
    global answer
    answer = 0

    dfs(numbers, target, 0)

    return answer