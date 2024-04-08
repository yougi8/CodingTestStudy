## 이코테 기출문제 그리디 2번 - 곱하기 혹은 더하기
# 숫자로만 이루어진 문자열 s가 주어졌을 때,
# 곱하기 혹은 더하기를 사용해서 만들 수 있는 가장 큰 수 구하기
# ( 곱하기 먼저라는 규칙은 없다. 앞에 있는 수식이 먼저 계산된다)

s = input()

result = 0
for i in range(len(s)):
    if s[i]==0:
        result += int(s[i])
    else:
        if result == 0:
            result = 1 * int(s[i])
        else:
            result = result * int(s[i])
print(result)

## input-output
# 02984 - 576
# 567 - 210
## 문제 풀이
# 0이 아닌 경우는 무조건 곱하기를 해야 숫자가 커진다고 생각했다
# 0일 경우에는 결과값에 더하면 된다.
