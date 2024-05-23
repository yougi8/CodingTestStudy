from itertools import permutations

def isPrime(n):
    if n==1 or n==0:
        return False
    # 2로 나누어 떨어지면 소수 아님
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True  # 소수면 True 반환

def solution(numbers):
    answer = 0
    arr = list(numbers)  # 17을 1 7 로 떼주기

    combi = []  # 조합 결과 저장할 배열
    for i in range(1, len(numbers) + 1):  # 1개부터 len(numbers) 까지 조합 결과 가능
        combi += permutations(arr, i)  # arr에서 i개 조합 찾기
    int_nums = list(set([int(''.join(t)) for t in combi])) # 숫자로 변환하기 ('1') -> 1 // ('1','7') -> 17 & 중복제거 (1,1,1) -> (1)

    print(int_nums)
    # 소수 찾기
    for i in range(len(int_nums)):
        print(int_nums[i])
        # 소수면 추가
        if isPrime(int_nums[i]):
            answer += 1

    print(answer)

solution("011")