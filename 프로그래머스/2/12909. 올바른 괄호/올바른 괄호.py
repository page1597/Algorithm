from collections import deque

def solution(s):
    temp = []
    stack = deque(list(s))
    
    while len(stack) != 0:
        popped = stack.popleft()
        if len(temp) == 0:
            # 아무것도 없을 경우 그냥 추가
            temp.append(popped)
            
        else:
            temp_popped = temp.pop()
            
            if temp_popped == ")":
                temp.append(temp_popped)
                temp.append(popped)
            elif temp_popped == "(" and popped == "(":
                # 짝이 맞지 않는 경우
                temp.append(temp_popped)
                temp.append(popped)
            
    answer = len(temp) == 0
    return answer
