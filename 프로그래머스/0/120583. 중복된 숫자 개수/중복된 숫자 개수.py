from collections import Counter

def solution(array, n):
    answer = Counter(array)[n]
    return answer