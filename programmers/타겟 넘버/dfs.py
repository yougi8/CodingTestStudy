# def dfs(numbers, target, idx, current_sum, count):
#     if idx == len(numbers):
#         if current_sum == target:
#             count += 1
#
#     dfs(numbers, target, idx + 1, current_sum + numbers[idx], count)
#     dfs(numbers, target, idx + 1, current_sum - numbers[idx], count)
#
#     return count

def dfs(numbers, target, idx, current_sum, count):
    if idx == len(numbers):
        if current_sum == target:
            return count + 1
        return count

    count = dfs(numbers, target, idx + 1, current_sum + numbers[idx], count)
    count = dfs(numbers, target, idx + 1, current_sum - numbers[idx], count)

    return count

def solution(numbers, target):
    return dfs(numbers, target, 0, 0, 0)


print(solution([1, 2], 1))




