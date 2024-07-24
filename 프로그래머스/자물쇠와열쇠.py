## 프로그래머스 - 자물쇠와 열쇠 (카카오 기출)

def solution(key, lock):
    n = len(key)
    m = len(lock)
    # 자물쇠의 상하좌우에 키만큼의 크기를 추가한 새로운 보드 만들기
    size = m + n * 2
    board = [[0] * size for _ in range(size)]
    for i in range(m):
        for j in range(m):
            board[i + n][j + n] = lock[i][j]

    # 열쇠 90도 회전
    def rotate(arr):
        result = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                result[i][j] = arr[n - j - 1][i]
        return result

    def search(key, x, y):
        answer = True
        for i in range(n):
            for j in range(n):
                board[i + x][j + y] += key[i][j]

        for i in range(m):
            if not answer: break

            for j in range(m):
                if board[n + i][n + j] != 1:
                    answer = False
                    break
        for i in range(n):
            for j in range(n):
                board[i + x][j + y] -= key[i][j]

        return answer

    for _ in range(4):
        key = rotate(key)

        for i in range(1, n + m):
            for j in range(1, n + m):
                if search(key, i, j): return True

    return False