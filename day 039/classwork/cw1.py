def sum_list(numbers):
    total = 0
    index = 0
    while index < len(numbers):
        total += numbers[index]
        index += 1
    return total