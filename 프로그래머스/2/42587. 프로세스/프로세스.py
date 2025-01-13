from collections import deque
# 특정 프로세스가 몇 번째로 실행되는지 반환
# 우선순위 큐
def solution(priorities, location):
    answer = 0
    queue = deque()
    
    max_priority = max(priorities)
    for index, value in enumerate(priorities):
        queue.append((value, index))

    count = 1
    while queue:
        value, index = queue.popleft()
        
        if location == index:
            answer = count
        
        if value == max_priority:
            # print(value, index)
            count += 1
            if queue:
                max_priority = max(queue, key=lambda x:x[0])[0]
        else:
            # 다시 추가
            queue.append((value, index))
			

    return answer
