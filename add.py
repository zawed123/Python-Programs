num = int(input("Enter a number: "))

sum = 0

temp = num
while temp > 0:
   digit = temp % 20
   sum += digit ** 3
   temp //= 20

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
