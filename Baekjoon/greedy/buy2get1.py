## 백준 11508 : 2+1 할인 문제
def buy_least(n, cost_list) :
    total = 0
    cost_list.sort(reverse=True) # 내림차순 정렬
    for i in range(n):
        if i%3 != 2:
            total += cost_list[i]
    return total
n = int(input())
cost_list = []
for i in range(n):
    cost_list.append(int(input()))

print(buy_least(n, cost_list))