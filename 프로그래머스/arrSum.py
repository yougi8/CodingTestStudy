## 프로그래머스 - 행렬의 덧셈 Lv1 (99 비기너 문제)

def solution(arr1, arr2):
    answer = [[0] * len(arr1[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i][j] += arr1[i][j] + arr2[i][j]

    return answer