## 이코테 기출문제 구현 - 8 문자열 재정렬
s = input()
string = []
number = []

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(len(s)):
    if s[i] in alpha:
        string.append(s[i])
    else:
        number.append(int(s[i]))

string.sort()
answer = ''.join(string)
answer += str(sum(number))

print(answer)

## input - output
# K1KA5CB7 - ABCKK13
# AJKDLSI412K4JSJ9D - ADDIJJJKKLSS20

## 문제 풀이
# s[i]값이 문자인지 확인 -> alpha에 있는 값인지 알면 됨
# 문자라면 string 배열에 추가
# 숫자라면 number 배열에 추가
# string 배열 sort하기
# answer에 string배열 리스트화시킨 값을 추가
# 그 후에, number 배열 합을 str으로 변환시켜서 answer에 추가
