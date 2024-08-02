## 프로그래머스 - 실습 - 해시 - 전화번호목록 https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    phone_book.sort()
    # print(phone_book)
    # for i in range(len(phone_book)):
    #     for j in range(len(phone_book)):
    #         if i==j or len(phone_book[i])>=len(phone_book[j]):
    #             continue
    #         length = len(phone_book[i])
    #         if phone_book[i] == phone_book[j][:length]:
    #             return False

    # for i in range(len(phone_book)):
    #     for j in range(i+1,len(phone_book)):
    #         length = len(phone_book[i])
    #         if phone_book[i] == phone_book[j][:length]:
    #             return False

    for i in range(len(phone_book) - 1):
        length = len(phone_book[i])
        if phone_book[i] == phone_book[i + 1][:length]:
            return False
    return True

## 위의 두개는, for문을 두번 돌기 때문에 시간이 O(n**2)이다. 상당히 비효율적. 그래서 효율성 테스트에서 50%만 정답이었다.
# 접두사랑 모든 번호를 비교하는게 아니고, 바로 다음 번호만 비교해도 된다! (왜인지는 잘 모르겠음 ㅠㅠ)

