n, c = map(int, input().split(' ')) # 하나 이상의 빈칸을 사이에 두고 주어진다.

array = []
for _ in range(n):
    array.append(int(input())) # array에 추가하기 : array네임.append(추가할 값)

array.sort() # 오름차순 정렬

