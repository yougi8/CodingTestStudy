n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort() # 리스트를 오름차순으로 정렬

first = data[n-1] # 가장 큰 숫자 : 리스트의 마지막 번째 숫자
second = data[n-2] # 두 번째로 큰 숫자 : 리스트의 마지막-1 번째 숫자

result = 0 # 결과값을 저장할 변수

result += (m//k) * (k*first) # 가장 큰 숫자는 m을 k로 나눈 몫만큼 연속으로 더해진다.
result += (m%k) * second # 두 번째로 큰 숫자는 m을 k로 나눈 나머지만큼 한 번씩 더해진다.

print(result)

## 잘못된 코드
## 이렇게 하면, first가 k번씩 연속하는게 아닌 k-1 번씩 연속하게 된다.
# for i in range(m):
#     if((i+1)/k!=0):
#         result += first
#     else:
#         result += second
