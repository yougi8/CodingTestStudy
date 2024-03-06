def change(n):
    result = 0

    while n > 0 :
        if n % 5 == 0 :
            result += n // 5
            n = n % 5
        else:
            result += 1
            n -= 2

    if n < 0 :
        print(-1)
    else :
        print(result)

n = int(input())
change(n)
