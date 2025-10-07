def is_even(nums):
    if nums % 2 == 0:
        return f'number <{nums}> is even'
    return f'number <{nums}> is odd'

nums = int(input('number: '))
print(is_even(nums))