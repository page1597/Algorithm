from collections import deque

def solution(numbers, target):
    def dfs(index, sum):
        if index == len(numbers):
            return 1 if sum == target else 0
        
        return dfs(index + 1, sum + numbers[index]) + dfs(index + 1, sum - numbers[index])
    
    answer = dfs(0, 0)
    return answer