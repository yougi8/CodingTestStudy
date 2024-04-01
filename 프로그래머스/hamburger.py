## 프로그래머스 연습문제 - 햄버거 만들기 (99클럽 미들러 문제) level 1
def solution(ingredient):
    answer = 0
    ## 1:빵 / 2:야채 / 3:고기 => 1231 찾기

    cook = []
    for i in ingredient:
        cook.append(i)

        ## cook 배열의 마지막 4개가 햄버거 재료 순서와 같다면 햄버거 만들기
        if cook[len(cook) - 4:len(cook)] == [1, 2, 3, 1]:
            answer += 1

            ## 햄버거 만들었으니까 재료 빼주기
            for _ in range(4):
                cook.pop()

    return answer

### 문제 풀이
# 말도 안되는 for-if문 4개를 이중삼중사중으로 써서, 테스트케이스 몇 개만 통과하고 당연히 시간초과가 났다..
# 그치만 이 코드를 짜느라 50분 가까이 썼는걸..? ㅠㅠ
# 정신 부여잡고 리스트 방식으로 해결해보았다.
# - list를 새로 만들어서 append 하고, 햄버거를 만들면 pop 하는 형식으로 해결함
# - 알아두면 좋을 것 : 나는 배열의 마지막 4개를 인덱싱할 때, `cook[len(cook)-4:len(cook)]` 이렇게 했지만, `cook[-4:]` 이렇게 하면 간단! 실수할 일도 없다!