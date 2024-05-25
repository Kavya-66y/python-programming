def multiplied_list(input_list):
    result = 1
    for num in input_list:
        result *= num
    return result
my_nums = [1,2,6,9,-3]
print(multiplied_list(my_nums))
