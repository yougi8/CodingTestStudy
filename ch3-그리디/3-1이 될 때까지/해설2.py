n,k = map(int, input().split())
result = 0

while True:
    # n==k로 나누어 떨어지는 수가 될 때까지 1씩 빼기
    ## n을 k로 나눈 후, 다시 k를 곱함으로써 n이 k로 나누어 떨어지는 가장 가까운 수를 찾음.
    target = (n//k) * k
    ## 그리고 이를 n에서 빼서 1을 빼는 연산의 횟수를 한번에 계산
    result += n - target
    n = target

    # n이 k보다 작을 때(더이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
## n은 k보다 작은 수이므로 더이상 k로 나눌 수 없음. 그러나 n은 아직 1이 아닐 수 있음.
## 따라서 n이 1이 될 때까지 n에서 1을 뺴는 연산을 수행해야 함.
## (n-1) : n에서 1을 빼는 연산을 수행해야 하는 횟수
result += (n-1)
print(result)