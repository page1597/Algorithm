def solution(numbers):
    str_arr = list(map(str, numbers))
    
    result = sorted(str_arr, key=lambda x: x*3, reverse=True)

    if result[0] == "0":
        answer = "0"
    else:
        answer = "".join(result)
    
    return answer
