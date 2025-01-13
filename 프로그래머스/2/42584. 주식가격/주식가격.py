from collections import deque

def solution(prices):
    answer = [0] * len(prices)
    stack = deque()

    for index, price in enumerate(prices):
        stack.append((price, index))

    while stack:
        current_price, current_index = stack.popleft()
        count = 0

        for next_price, _ in list(stack):
            count += 1
            if current_price > next_price:
                break

        answer[current_index] = count

    return answer
