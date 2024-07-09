def solution(arr):
    answer = [0, 0]

    # 영역 시작위치x(좌상단), 시작위치y(좌상단), 한변의 길이
    def quad(x, y, l):
        number = arr[x][y]
        for i in range(x, x + l):
            for j in range(y, y + l):
                if arr[i][j] != number:
                    l = l // 2
                    print(l)
                    quad(i, j, l)  # 좌상단
                    quad(i, j + l, l)  # 좌하단
                    # quad(i+l, j, l) # 우상단
                    # quad(i+l, j+l, l) # 우하단
                    return
        answer[number] += 1

    quad(0, 0, len(arr))

    # for i in range(len(arr)):
    #     for j in range(len(arr[i])):
    #         if arr[i][j] == 0:
    #             answer[0] += 1
    #         else:
    #             answer[1] += 1

    print(answer)
input = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
solution(input)
