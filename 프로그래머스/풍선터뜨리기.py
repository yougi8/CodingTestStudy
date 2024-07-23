## 프로그래머스 - 풍선터뜨리기
def solution(a):
    answer = 2  # 양쪽 끝값들은 살아남을 수 있음
    n = len(a)
    l_min = [a[0]]
    r_min = [a[-1]]

    for i in range(1, n):
        # 왼쪽 최솟값 구하기
        if a[i] < l_min[-1]:
            l_min.append(a[i])
        else:
            l_min.append(l_min[-1])

        # 오른쪽 최솟값 구하기
        if a[n - i - 1] < r_min[-1]:
            r_min.append(a[n - i - 1])
        else:
            r_min.append(r_min[-1])

    r_min.reverse()

    for i in range(1, n - 1):
        if a[i] < l_min[i - 1] or a[i] < r_min[i + 1]:
            answer += 1

    return answer