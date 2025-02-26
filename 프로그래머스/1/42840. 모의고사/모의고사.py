def solution(answers):
    answer = []
    pattern_1 = [1, 2, 3, 4, 5]
    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for pattern in [pattern_1, pattern_2, pattern_3]:
        count = 0
        for i in range(len(answers)):
            if pattern[i % len(pattern)] == answers[i]:
                count += 1
        answer.append(count)
    max_value = max(answer)
    max_indexes = [i+1 for i, v in enumerate(answer) if v == max_value]
    return sorted(max_indexes)
