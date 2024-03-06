## 백준 2217번
import sys
def rope(n, weight):
    max_value = [0]*n
    weight.sort(reverse=True) # 내림차순 정렬
    for i in range(n):
        max_value[i] = weight[i] * (i+1)
    return max(max_value)

n = int(sys.stdin.readline())
weight = [0]*n
for i in range(n):
    weight[i] = int(sys.stdin.readline())
print(rope(n, weight))