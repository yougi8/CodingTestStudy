## 프로그래머스  - 기사단원의 무기 - Lv1 (99클럽 미들러 문제)

# 약수의 개수를 구해야 한다.
def solution(number, limit, power):
    # 1은 약수가 1개 이므로, 공격력은 1이 된다.
    # 그러므로 limit을 넘지않으니 결과값에 미리 추가한다
    answer = 1

    def find(num):
        total = 2  # 자기자신과 1은 기본적으로 약수로 가진다.
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                if i == num ** 0.5:  # 제곱근이면 한번만 더해주기
                    total += 1
                else:
                    total += 2  # 제곱근이 아니면 두번 더해주기
        return total

    for i in range(2, number + 1):
        total = find(i)
        if total > limit:
            answer += power
        else:
            answer += total

    return answer

## 문제풀이
# 약수의 개수는, n까지 돌면서 0으로 나누어떨어지는지 확인하면 된다.
# 이때 for문을 n까지 확인하면, 시간초과가 난다.
# 약수는 제곱근을 기준으로 대칭이라는 특징이 있다.
# 또한 1과 자기자신을 약수로 가진다.
# 때문에 약수는 기본으로 2개를 가진다. (2이상인 수 일때)
# for문을 2부터 제곱근까지 돌면서, 0으로 나누어떨어지는지 확인한다.
# 나누어떨어진다면, 제곱수인가 확인하고, 제곱수면 1증가, 제곱수가 아니면 대칭인 수가 존재하니까 2추가 한다.
# 제곱근 구하기 : n**0.5