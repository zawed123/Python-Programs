# https://www.facebook.com/manshu.rawat/posts/3347299632030687
# subscribed by manshu
order = len(str(num))

sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
