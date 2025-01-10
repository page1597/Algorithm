def solution(arr):
    answer = []
    std = -999
    for el in arr:
        if std != el:
            answer.append(el)
            std = el
    return answer
