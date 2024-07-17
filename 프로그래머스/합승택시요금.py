## 프로그래머스 - 합승택시요금
def solution(n, s, a, b, fares):
    answer = int(1e9)
    INF = int(1e9)
    arr = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j: arr[i][j] = 0
    for x, y, c in fares:
        arr[x][y] = c
        arr[y][x] = c

    # 1-4 로 가는데, 1-4가 작은지, 1-2 + 2-4 가 더 작은지 비교해서 값 할당 (모든 경로를 최소값으로 바꿔주기)
    for i in range(1, n + 1):
        for x in range(1, n + 1):
            if x == i: continue
            for y in range(1, n + 1):
                if y == i: continue
                arr[x][y] = min(arr[x][y], arr[x][i] + arr[i][y])

    # 합승 끝나는 지점?을 1부터 n까지 하나씩 설정해보면서, 어디까지가 최소인지 확인해보기
    for i in range(1, n + 1):
        answer = min(arr[s][i] + arr[i][a] + arr[i][b], answer)
    return answer

solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])

# 처음에 플로이드-워셜 방법 썼다가, 합승구간에 대한 해결책이 나오지 않아서 방법을 바꿔야하나 생각했다.
# 그치만, 합승구간을 1부터 n까지 임의로 설정하고 그 구간을 거치는 최소값을 찾으면 정답! 이었다.
# n	s	a	b	fares	result
# 6	4	6	2	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]	82
# 7	3	4	1	[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]	14
# 6	4	5	6	[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]	18