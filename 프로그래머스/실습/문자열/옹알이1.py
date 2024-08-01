## 프로그래머스 도서 실습 - 문자열 다루기 - 옹알이1
def solution(babbling):
    answer = 0
    possible = ['aya', 'ye', 'woo', 'ma']

    for babble in babbling:
        length = len(babble)
        cnt = 0
        for i in range(4):
            if possible[i] in babble:
                cnt += len(possible[i])
        if cnt == length:
            answer += 1
    return answer