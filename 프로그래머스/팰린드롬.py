## 프로그래머스 - 가장 긴 팰린드롬 https://school.programmers.co.kr/learn/courses/30/lessons/12904
def solution(s):
    n = len(s)
    if n == 1: return 1

    def search(left, right):
        # index(leff,right)를 기준으로 왼쪽 오른쪽으로 하나씩 확장해가면서 값이 달라질 때까지 살펴본다
        # 왼쪽, 오른쪽값이 달라지는 순간이 팰린드롬이 끝나는 순간!
        # 해당 인덱스 번호를 통해서 팰린드롬의 길이를 return 해준다.
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    answer = 0
    for i in range(n):
        len1 = search(i, i)  # 팰린드롬이 홀수길이일 때 (ex. aba, abcdcba)
        len2 = search(i, i + 1)  # 팰린드롬이 짝수길이일 때 (ex.abba, acddbbddec)
        answer = max(answer, len1, len2)

    return answer

## 처음 생각 : 팰린드롬의 길이가 짝수인 경우는 생각 못하고, 홀수일 때만 생각했다. (index가 한개)
## 이렇게 하면 짝수인 경우를 체크하지 못한다! 그리고 복잡하게 문자열 인덱싱 안하고 값이 달라지는 순간까지의 길이만 구하면 된다
# def solution(s):
#     answer = 0

#     def check(start, end, max_value):
#         left = s[start:end]
#         right = s[end+1:end+(end-start)+1]
#         n_right = right[::-1]

#         if left==n_right:
#             length = len(left)*2 + 1
#             if length>max_value:
#                 return length
#         return max_value


#     for i in range(1, len(s)):
#         for j in range(i-1,-1,-1):
#             answer = check(j,i,answer)
#         if answer==len(s):
#             return answer

#     return answer