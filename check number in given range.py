def check_num(num):
    lower = 1
    upper = 10
    if lower <= num <= upper:
            return num 
    else:
            print('num is not existed')

num = int(input('enter a number'))
print(check_num(num))
