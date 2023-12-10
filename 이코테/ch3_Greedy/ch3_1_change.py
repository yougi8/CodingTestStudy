n = 1260 # 총 금액
count = 0 # 손님에게 줄 동전 개수

coin_types = [500,100,50,10] # 동전 단위 저장

for coin in coin_types: # 동전 종류만큼 반복
    count += n // coin # 남은 총 금액을 각 동전 단위로 나눈 몫을 저장 (count)
    n %= coin # 다음 계산할 총 금액은, 먼저 계산한 값의 나머지 값.

print(count) # 총 거스름돈 개수 출력