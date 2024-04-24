def is_palindrome(num):
    return num == num[::-1]
num = '120'
result = is_palindrome(num)
if result:
    print('it is palindrome')
else:
    print('it is not palindrome')
