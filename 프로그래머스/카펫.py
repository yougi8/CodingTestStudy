## 프로그래머스 - Lv2. 카펫 https://school.programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    if yellow == 1:
        return [3, 3]

    answer = []
    have = []

    for i in range(1, yellow // 2 + 1):
        if yellow % i == 0:
            if i > yellow // i:
                break
            have.append((i, yellow // i))
    for w, h in have:
        size = (w + 2) * (h + 2) - yellow
        if size == brown:
            return [h + 2, w + 2]
    return answer

## 완전탐색 유형이라는데, 나는 그냥 구현같음.