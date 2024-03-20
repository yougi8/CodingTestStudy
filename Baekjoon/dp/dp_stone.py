## 백준 dp 실버5 - 9655 돌 게임
import sys
n = int(sys.stdin.readline())

## dp 사용 안하고 그냥 게임 결과를 따지다보니, 홀짝으로만 나누어지는 게임이었다.
if n%2 == 0:
    print("CY")
else:
    print("SK")