import sys
n = sys.stdin.readline()

length = len(n)-1

sum1 = 0
sum2 = 0

for i in range(0,int(length/2)):
    sum1 += int(n[i])
for i in range(int(length/2), length):
    sum2 += int(n[i])
if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")