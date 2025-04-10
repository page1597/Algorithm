def solution(n, lost, reserve):
    index = 0
    lost_array = list(set(lost) - set(reserve))
    reserve_array = list(set(reserve) - set(lost))
    reserve = sorted(reserve_array)
    lost = sorted(lost_array)
    answer = n - len(lost)
    
    while index < len(lost):
        
        if lost[index]-1 in reserve:
            reserve.remove(lost[index]-1)
            answer += 1
            index += 1
            
        elif lost[index]+1 in reserve:
            reserve.remove(lost[index]+1)
            answer += 1
            index += 1
        else:
            index += 1
        
    return answer