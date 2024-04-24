def myfunc(*args):
    return [arg for arg in args if arg % 2 == 0]

result = myfunc(5, 6, 7, 8)
print(result)  

    
