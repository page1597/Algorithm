def solution(numbers, direction):
    answer = []
    concat_arr = numbers + numbers
    print(concat_arr)
    if direction == "right":
        answer = concat_arr[len(numbers)-1: len(numbers)-1+len(numbers)]
    else:
        answer = concat_arr[1: len(numbers)+1]
    return answer