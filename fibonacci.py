n = 10
n1 = 0
n2 = 1
next_num = n2
count = 1
while count<n:
    print(next_num)
    count+=1
    n1 = n2
    n2 = next_num
    next_num = n1+n2
print()