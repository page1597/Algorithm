import re
from functools import reduce
def solution(my_string):
    answer = 0
    num_arr = re.findall(r'\d+', my_string)
    if (len(num_arr) == 0):
        answer = 0
    else:
        answer = reduce(lambda x, y: x + y, map(int, num_arr))
    return answer