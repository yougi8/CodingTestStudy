def dfs(numbers, target, idx, current_sum):
    if idx == len(numbers):
        if current_sum == target:
            return 1 # count 값 return
        else:
            return 0 # # count 값 return
    else:
        return dfs(numbers, target, idx + 1, current_sum + numbers[idx]) + dfs(numbers, target, idx + 1, current_sum - numbers[idx])

def solution(numbers, target):
    return dfs(numbers, target, 0, 0)

print(solution([1, 2], 1))