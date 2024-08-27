## 프로그래머스 - 파괴되지 않은 건물 Lv.3 https://school.programmers.co.kr/learn/courses/30/lessons/92344
def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    arr = [[0] * (m + 1) for _ in range(n + 1)]

    # 누적합 구할 새로운 배열 생성하기
    for do in skill:
        act = do[0]  # 공격:1, 회복:2
        x1, y1 = do[1], do[2]
        x2, y2 = do[3], do[4]
        degree = do[5]

        if act == 1:
            arr[x1][y1] -= degree
            arr[x2 + 1][y2 + 1] -= degree
            arr[x1][y2 + 1] += degree
            arr[x2 + 1][y1] += degree
        else:
            arr[x1][y1] += degree
            arr[x2 + 1][y2 + 1] += degree
            arr[x1][y2 + 1] -= degree
            arr[x2 + 1][y1] -= degree

    # 2차원 배열 누적합 계산하기
    for i in range(1, len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] += arr[i - 1][j]
    for i in range(len(arr)):
        for j in range(1, len(arr[0])):
            arr[i][j] += arr[i][j - 1]

    ## 파괴 건물 수 구하기
    for i in range(n):
        for j in range(m):
            if board[i][j] + arr[i][j] >= 1:
                answer += 1
    return answer

## 문제 풀이
# 누적합을 이용해서 문제를 풀어야 효율성 테스트를 통과한다.
# 누적합이란, a부터 b까지 c만큼의 크기변화를 주고싶다면, 새로운 배열을 만들어서 a번째에 +c, b+1번째에 -c를 한 후에 누적합을 구하고
# 기존 배열과 새로운 배열을 더하면 된다! -> 시간복잡도를 줄일 수 있다.
# 2차원 배열에서 누적합운, (a,b) 부터 (c,d) 까지 k만큼 변화를 주고싶다면
# (a,b), (c+1,d+1)자리에 +k를 하고, (a,d+1),(b,c+1) 자리에 -k를 한 새로운 배열을 만들어서
# 세로로 누적합 구하고, 가로로 누적합 구한 후에
# 기존 배열과 합치면 된다.

## 누적합을 사용하지 않고 푼 코드는 정확성 테스트만 통과한다.
# def solution(board, skill):
#     answer = 0
#     n = len(board)
#     m = len(board[0])
#
#     for do in skill:
#         act = do[0] # 공격:1, 회복:2
#         x1, y1 = do[1],do[2]
#         x2, y2 = do[3],do[4]
#         degree = do[5]
#
#         for i in range(x1,x2+1):
#             for j in range(y1,y2+1):
#                 if act==1:
#                     board[i][j] -= degree
#                 else:
#                     board[i][j] += degree
#
#     ## 파괴 건물 수 구하기
#     for i in range(n):
#         for j in range(m):
#             if board[i][j]>=1:
#                 answer += 1
#     return answer