def find_short(route1, route2):
    min1 = route1[0]
    min2 = route2[0]

    for route in route1:
        if route < min1:
            min1 = route
    for route in route2:
        if route < min2:
            min2 = route

    print('첫번째 최단거리 : ', min1)
    print('두번째 최단거리 : ', min2)

    #  최단거리 합 return
    return min1 + min2

# 첫 번째 경로의 리스트 / 두 번째 경로의 리스트
arr1 = list(map(int, input().split(',')))
arr2 = list(map(int, input().split(',')))

print('최단경로 : ', find_short(arr1, arr2))