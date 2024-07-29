def solution(array, height):
    answer = 0
    filtered = filter(lambda x: x > height, array)
    answer = len(list(filtered))
    return answer