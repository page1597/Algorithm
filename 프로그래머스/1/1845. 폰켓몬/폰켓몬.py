def solution(nums):
    n = len(nums)/2  
    answer = min(len(set(nums)), n)
    return answer