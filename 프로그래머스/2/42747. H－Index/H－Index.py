def solution(citations):
    sorted_arr = sorted(citations)
    reversed_sorted_arr = sorted(citations, reverse=True)
    if len(citations) < sorted_arr[0]:
        answer = len(citations)
    else:
        count = 0
        for i in reversed_sorted_arr:
            if i > count:
                count += 1
        
        answer = count
    
    return answer
