import sys
n = int(sys.stdin.readline())

total = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            hour = str(i)+str(j)+str(k)
            if '3' in hour:
                total += 1
print(total)