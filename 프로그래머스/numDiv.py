def cal(a, b):  # 최대 공약수 구하기
    if a % b == 0:
        return b
    return cal(b, a % b)  # 35 = 17*2 + 1 인 것을 생각!

def solution(arrayA, arrayB):
    a = arrayA[0]
    b = arrayB[0]

    for i in range(1, len(arrayA)):
        a = cal(arrayA[i], a)
        b = cal(arrayB[i], b)

    answerA = a
    answerB = b

    # 최대공약수가 다른 숫자카드와 나누어 떨어지는지 확인
    for i in range(len(arrayA)):
        if arrayA[i] % b == 0:  # 영희 숫자카드가 철수 숫자를 나누는지 확인
            answerB = 0
        if arrayB[i] % a == 0:  # 철수 숫자카드가 영희 숫자를 나누는지 확인
            answerA = 0

    return max(answerA, answerB)