def find_shortest_distance(ways):
    shortest = ways[0]
    for way in ways:
        if way < shortest:
            shortest = way
    return shortest

first_way = list(map(int, input().split()))
second_way = list(map(int, input().split()))

first_min = find_shortest_distance(first_way)
second_min = find_shortest_distance(second_way)

print(first_min + second_min, "km")

