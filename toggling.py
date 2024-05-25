n = int(input('enter the value of n'))
binary = bin(n)[2:]
st = ""
for i in binary:
    if i == '1':
        st += '0'
    else:
        st += '1'
print(int(st,2))
