# https://www.facebook.com/graeyaki/posts/3604553256276181
# Subscribed by Pranav Kumar Mishra


my_str = 'aIbohPhoBiA'

my_str = my_str.casefold()

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
