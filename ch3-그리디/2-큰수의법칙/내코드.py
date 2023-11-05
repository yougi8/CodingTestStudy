n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0
count = 1
while True: # 숫자가 더해지는 횟수

    # 반복문 나가기
    if count > m:
        break

    if count % k != 0:
        result += first
    else:
        result += second

    count += 1

print(result)

############################################################
# <오답>
# [문제 이해]
# 처음에는 잘못 이해해서, 6+6+6+5+5+5+4 로 결과가 나왔음
# 큰 수를 더하면, 그 큰 수는 덧셈에서 빠지는 걸로 착각해버림

# [큰 수 & 2번째로 큰 수 구하는 법]
# 큰 수만 구하고, 그 큰 수를 배열에서 뺄 생각만 함
# => 정렬을 이용해 큰 수, 2번째 큰 수를 변수로 지정할 것!

# ['내코드'의 주의점]
# count를 1로 해야지 올바르게 로직이 돌아감

# <해설1>
# count라는 변수를 따로 만들지 않고, input으로 받은 m변수 통해 반복문 탈출 가능!
# 내코드는 if문으로 'count % k != 0'조건을 줬고
# 해설1은 k(input값=숫자가 더해지는 횟수)를 for문으로 돌려 if문이 필요하지 않았음

# <해설2>
# 시간 초과 판정을 피하기 위한 방법
# 중요 식 : (m//(k+1))*k + m%(k+1)

