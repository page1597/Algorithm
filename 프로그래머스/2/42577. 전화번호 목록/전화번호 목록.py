def solution(phone_book):
    sorted_phone_book = sorted(phone_book)

    for index, _ in enumerate(sorted_phone_book):
        if index == len(sorted_phone_book) - 1:
            break
        if sorted_phone_book[index] == sorted_phone_book[index+1][:len(sorted_phone_book[index])]:
            return False
    return True