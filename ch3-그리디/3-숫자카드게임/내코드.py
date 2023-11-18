n,m = map(int, input().split())
# arr = []
min_values = []
result = 0

for _ in range(n):
    line = list(map(int, input().split()))
    if len(line) != m:
        print("입력한 숫자의 개수 올바르지 않습니다.")
        break

    # arr.append(line)
    min_values.append(min(line))


# print(arr)
# print("min_values", min_values)
result = max(min_values)
print(result)

#######################################
# 1. 2차원 배열이므로, 행 하나 받을 때마다 가장 작은 값을 min_value 배열에 저장
# 2. for문(input 값을) 모두 돌면(받으면) min_value 배열 중에서 가장 max 값  찾기 (result)

#<해설>
# min_values 배열, result를 따로 만들 필요 X
# result에 max 함수를 사용해서 바로 값 얻어올 수 있음! => result = max(result, min_value)