#  https://www.facebook.com/graeyaki/posts/3604553256276181
# Subscribed by Pranav Kumar Mishra

import cmath

num = eval(input('Enter a number: '))


num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))
