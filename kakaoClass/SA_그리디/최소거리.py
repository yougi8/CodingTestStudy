first_way = list(map(int, input().split()))
second_way = list(map(int, input().split()))

first_min = first_way[0]
second_min = second_way[0]

for i in range(len(first_way)) :
    if first_min > first_way[i]:
        first_min = first_way[i]

for i in range(len(second_way)) :
    if second_min > second_way[i]:
        second_min = second_way[i]

print(first_min + second_min, "km")
