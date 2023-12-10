n, m = map(int, input().split())

result = 0
min = 0

for i in range(n):
    card = map(int, input().split())

    min_value = 10001

    for j in card:
        min_value = min(min_value,j)

    