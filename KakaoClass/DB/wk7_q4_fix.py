def fix_value(array, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return fix_value(array, start, mid-1)
    else:
        return fix_value(array, mid+1, end)
    
n = int(input())
array = list(map(int, input().split()))

result = fix_value(array, 0, n-1)

if result == None:
    print(-1)
else:
    print(result)