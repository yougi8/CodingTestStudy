def apple_game(m, apple):
    pos = 1
    move = 0

    for i in apple :
        if pos <= i and pos + m-1 >= i : # 떨어지는 사과가 내 위치보다 오른쪽에 있고, 내 위치 +바구니 크기보다 왼쪽에 있으면 이동 x
            continue
        elif pos + m-1 < i : # 오른쪽으로 떨어지는 경우
            move += (i - (pos + m-1))
            pos += (i - (pos + m-1))
        else : # 왼쪽으로 떨어지는 경우
            move += (pos - i)
            pos -= (pos - i)

    print(move)

n, m = map(int, input().split()) # 스크린의 크기 N, 바구니의 크기 M
j = int(input()) # 떨어지는 사과의 개수

apple = [] # 떨어지는 사과의 위치 리스트

for i in range(j) :
    apple.append(int(input()))

apple_game(m, apple)
