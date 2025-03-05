def solution(brown, yellow):
    total_block_count = brown + yellow

    answers_set = set()

    for i in range(1, total_block_count+1):
        if total_block_count % i == 0:
            answers_set.add(tuple(sorted((i, int(total_block_count / i)))))

    for (a, b) in answers_set:
        if (a - 2) * (b - 2) == yellow:
            answer = (a, b)
    return sorted(list(answer), reverse=True)

