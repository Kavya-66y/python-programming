def fact(n):
    if n<0:
        return 0
    elif n==0 | n==1:
        return 1
    else:
        fact = 1
        while(n>0):
            fact = fact*n
            n = n-1
        return fact
n = 10
result = fact(n)
print('result of {} is {}'.format(10,fact(n)))

