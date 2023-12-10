import sys
input = sys.stdin.readline()

alpha = input[0]
number = int(input[1])

## 알파벳을 숫자로 바꾸는 법을 몰라서 그냥 냅다 하드코딩
alphabet = ['a','b','c','d','e','f','g','h']
for i in range(len(alphabet)):
    if alpha == alphabet[i]:
        alpha = i+1
        break
moves = [(-1, -2), (1, -2), (-1, 2), (1, 2), (-2, 1), (-2, -1), (2, 1), (2, -1)] # 가로세로 이동의 경우 8가지
print('alpha : ',alpha)
total = 0
for i in moves:
    if alpha + i[1] < 1 or alpha + i[1] >8 or number + i[0] < 1 or number + i[0] >8 :
        continue
    total += 1
print(total)