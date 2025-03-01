from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numberList = list(numbers)
    permutationSet = set()

    for length in range(1, len(numberList) + 1):
        for perm in permutations(numberList, length):
            permutationSet.add(int("".join(perm)))
    primes = list(num for num in permutationSet if is_prime(num))
    answer = len(primes)
    return answer
