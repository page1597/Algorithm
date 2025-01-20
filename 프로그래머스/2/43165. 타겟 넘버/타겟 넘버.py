from collections import deque

def solution(numbers, target):
    queue = deque([(0, 0)])
    count = 0
    
    while queue:
        index, sum = queue.pop()
        
        if index == len(numbers):
            if sum == target:
                count += 1
        else:
            queue.append((index + 1, sum + numbers[index]))
            queue.append((index + 1, sum - numbers[index]))
    answer = count
    return answer