## 이코테 기출문제 구현 - 8 문자열 재정렬 (프로그래머스 60057)
# 1개 이상 단위로 문자열을 잘라 가장 짧게 압축한 길이
# 1 <= s <= 1000. 소문자로만 구성

def solution(s):
    answer = len(s)

    for size in range(1, len(s) // 2 + 1):
        new_string = ""
        prev = s[:size]

        count = 1  # 몇번 겹치는지 기록하는 숫자

        for i in range(size, len(s), size):
            if s[i:i + size] == prev:
                count += 1
            else:
                if count >= 2:
                    new_string += str(count) + prev
                else:
                    new_string += prev
                prev = s[i:i + size]
                count = 1

        if count >= 2:
            new_string += str(count) + prev
        else:
            new_string += prev
        answer = min(answer, len(new_string))

    return answer