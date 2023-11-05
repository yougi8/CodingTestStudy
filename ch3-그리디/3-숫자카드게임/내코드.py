n,m,k = map(int, input().split()) # n:개수 m:더하는 개수 k:연속 수
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k): # 가장 큰 수 더하기
        if(m==0):
            break
        result += first
        m -= 1

    if(m==0):
        break
    result += second
    m -= 1

print(result)



