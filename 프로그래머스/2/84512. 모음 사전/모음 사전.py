def solution(word):
    answer = 0
    vowels = ["A", "E", "I", "O", "U"]
    orders = [781, 156, 31, 6, 1]

    for i, v in enumerate(word):
        index = vowels.index(v)
        answer += orders[i] * index + 1  
    return answer