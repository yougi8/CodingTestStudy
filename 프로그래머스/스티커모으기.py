## 프로그래머스 - 스티커 모으기(2) Lv3
def solution(sticker):
    # 길이가 1이면 걔가 최댓값
    if len(sticker) == 1:
        return sticker[0]

    # 길이가 2이면 1,2 중 최댓값이 정답
    if len(sticker) == 2:
        return max(sticker[0], sticker[1])

    # 첫번째 인덱스 선택 (마지막 인덱스를 선택할 수 없다)
    dp1 = sticker[:-1]
    dp1[1] = max(dp1[0], dp1[1])
    for i in range(2, len(dp1)):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + dp1[i])

    # 두번째 인덱스부터 선택 (마지막 인덱스 선택 가능)
    dp2 = sticker[1:]
    for i in range(2, len(dp2)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + dp2[i])

    # print(dp1)
    # print(dp2)
    return max(max(dp1), max(dp2))

# solution([4,3,2,9,4]) # answer: 13
# solution([14, 6, 5, 11, 3, 9, 2, 10]) # answer: 36
# solution([1, 3, 2, 5, 4]) # answer : 8
