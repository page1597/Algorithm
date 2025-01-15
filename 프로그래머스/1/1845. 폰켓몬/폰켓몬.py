def solution(nums):
    dict = {key: 0 for key in nums}
    n = len(nums)/2  
    for num in nums:
        dict[num] += 1
    count = len([value for value in dict.values() if value != 0])
    answer = min(count, n)
    return answer
