def solution(clothes):
    hash = {}
    for item in clothes:
        if item[1] in hash:
            hash[item[1]].append(item[0])
        else:
            hash[item[1]] = [item[0]]
    answer = 1
    for category in hash.values():
        answer *= len(category) + 1  

    return answer - 1