import math
from collections import Counter
def solution(progresses, speeds):
    temp = list(map(lambda x: 100 - x, progresses))
    print(temp)
    temp2 = []
    for index, speed in enumerate(speeds):
        n =  math.ceil(temp[index] / speed)
        temp2.append(n)

    biggerNum = 0
    for index, value in enumerate(temp2):
        if biggerNum < value:
            biggerNum = value
        if value < biggerNum:
            temp2[index] = biggerNum
    
    temp3 = list(Counter(temp2).values())
        
    answer = temp3
    return answer