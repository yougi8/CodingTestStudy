import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort(reverse=True)

group = 0
people = 0
goal = n
for i in range(n):
    if (n-i) == goal:
        people = arr[i]
        group += 1
        goal = n-i-people

print(group)