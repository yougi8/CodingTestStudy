## 프로그래머스 땅따먹기
def solution(land):
    answer = 0
    n = len(land)

    for i in range(1, n):
        for j in range(4):
            max_value = 0
            for k in range(4):
                if j == k: continue
                max_value = max(max_value, land[i - 1][k])
            land[i][j] += max_value
    # print(land)

    # 엄청나게 쉬운 코드 : 어차피 비교할 값이 본인 제외하고 3개뿐이니까 하드코딩으로 박아버리기
    #     for i in range(1, n):
    #         land[i][0] += max(land[i-1][1],land[i-1][2],land[i-1][3])
    #         land[i][1] += max(land[i-1][0],land[i-1][2],land[i-1][3])
    #         land[i][2] += max(land[i-1][0],land[i-1][1],land[i-1][3])
    #         land[i][3] += max(land[i-1][0],land[i-1][1],land[i-1][2])


    return max(land[n - 1])