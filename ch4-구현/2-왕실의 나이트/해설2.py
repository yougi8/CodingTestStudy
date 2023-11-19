# <dx와 dy 리스트를 사용해 각각 x과 y축으로 이동할 변화량을 나타내게 해서 문제 풀기>
# 상하좌우 문제와 같은 형식으로 풀기

input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

count = 0

for i in range(len(dx)):
    nrow = row + dx[i]
    ncol = col + dy[i]

    if nrow < 1 or ncol < 1 or nrow > 8 or ncol > 8:
        continue

    count += 1

print(count)