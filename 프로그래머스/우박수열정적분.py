## 프로그래머스 - 우박수열 정적분 Lv2. https://school.programmers.co.kr/learn/courses/30/lessons/134239
def solution(k, ranges):
    answer = []
    collatz = [k]  # 콜라츠 추측
    size = []  # 구간별 면적

    ## 콜라츠 추측 구하기
    cnt = k
    while cnt > 1:
        if cnt % 2 == 0:
            cnt = cnt // 2
            collatz.append(cnt)
        else:
            cnt = cnt * 3 + 1
            collatz.append(cnt)
    n = len(collatz) - 1

    ## 구간별 면적 구하기
    for i in range(len(collatz) - 1):
        a = collatz[i]
        b = collatz[i + 1]
        # 사다리꼴로 면적 구해서 면적 배열에 넣기
        size.append((a + b) / 2)

    for ran in ranges:
        x1 = ran[0]
        x2 = ran[1]
        if x1 == 0 and x2 == 0:
            answer.append(sum(size))
            continue

        x2 = n + ran[1]
        if x1 == x2:
            answer.append(0)
        elif x1 > x2:
            answer.append(-1)
        else:
            answer.append(sum(size[x1:x2]))
    return answer

solution(5, [[0,0],[0,-1],[2,-3],[3,-3]])

## 해설
# 그냥 구현,수학으로 풀었다
# x는 간격이 1이니까, 그 간격마다 넓이를 구한 배열을 만들어놓고
# 범위를 나눠서 합을 구한다!