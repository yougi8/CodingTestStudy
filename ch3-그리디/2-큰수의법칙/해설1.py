n,m,k = map(int, input().split()) # 배열의 크기 / 숫자가 더해지는 횟수 / 법칙
data = list(map(int, input().split()))

data.sort()
first = data[n-1] # 가장 큰 수
second = data[n-2] # 2번째로 큰 수

result = 0

while True:
    if m == 0: # m이 0이라면 반복문 탈출
        break

    for i in range(k): # 가장 큰 수를 k번 더하기
        if m == 0: # m이 0이라면 반복문 탈출
            break

        result += first
        m -= 1

    result += second # 2번째로 큰 수를 한 번 더하기
    m -= 1


print(result)


