import sys

def move(n, plan):
    pos = [1,1]

    for i in plan:
        if i == 'L':
            if pos[1]-1 <= 0:
                continue
            else:
                pos[1] -= 1
        elif i == 'R':
            if pos[1]+1 > n:
                continue
            else:
                pos[1] += 1
        elif i == 'U':
            if pos[0]-1 <= 0:
                continue
            else:
                pos[0] -= 1
        else:
            if pos[0]+1 > n:
                continue
            else:
                pos[0] += 1
    print(pos[0], pos[1])

n = int(sys.stdin.readline())
plan = list(map(str, sys.stdin.readline().split()))
new_plan = []
move(n,plan)