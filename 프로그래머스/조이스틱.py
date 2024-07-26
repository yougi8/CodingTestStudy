## 프로그래머스 - 조이스틱
def solution(name):
    answer = 0
    alpha = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
             'N': 13, 'O': 12, 'P': 11, 'Q': 10, 'R': 9, 'S': 8, 'T': 7, 'U': 6, 'V': 5, 'W': 4, 'X': 3, 'Y': 2, 'Z': 1}

    cursor_move = len(name) - 1

    for i, spell in enumerate(name):
        answer += alpha[spell]

        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        cursor_move = min(cursor_move, i + len(name) - next + min(i, len(name) - next))
    return answer + cursor_move
