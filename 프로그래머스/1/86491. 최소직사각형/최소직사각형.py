def solution(sizes):
    answer = 0
    for size in sizes:
        if size[0] < size[1]:
            temp = size[0]
            size[0] = size[1]
            size[1] = temp # 자리변경

    max_0 = max(size[0] for size in sizes)
    max_1 = max(size[1] for size in sizes)    
    answer = max_0 * max_1 
    
    return answer