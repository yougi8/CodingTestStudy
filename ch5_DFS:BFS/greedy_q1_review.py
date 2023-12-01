import sys
distance1 = list(map(int, sys.stdin.readline(). split()))
distance2 = list(map(int, sys.stdin.readline().split()))

min1 = distance1[0]
min2 = distance2[0]
for now in distance1:
    if now < min1:
        min1 = now
for now in distance2:
    if now < min2:
        min2 = now

print(min1 + min2)
