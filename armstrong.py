num = int(input('enter a number'))
order = len(str(num))
total = 0
temp = num
while temp > 0:
   digit = temp % 10
   total += digit**order
   temp //=10
if num == total:
   print(num,"is an armstrong number")
else:
   print(num,"is not an armstong number")