 # https://www.facebook.com/abhishek.dobliyal.5895/posts/104471008093195
 # Subscribed by Abhishek Dobliyal

## Program to count characters in a string

# Method 1

s1 = input("Enter a string: ")

count = {}
for char in s1:
    if char not in d:
        d[char] = 1
    else:
        d[char] += 1

print(count)


# Method 2

from collections import Counter

s2 = input("Enter a string: ")
print(Counter(s))
